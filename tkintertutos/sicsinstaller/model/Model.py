from time import sleep


class ReplaceFileThread(threading.Thread):
    def __init__(self, model, element, duration):
        threading.Thread.__init__(self)
        self.model = model
        self.element = element
        self.duration = duration
        self.msg = f"Copying {self.element}"

    def run(self):
        while self.duration >= 0:
            self.model.modelEvent.onInfoLabelUpdate(self.msg)
            sleep(1)


class Model:
    def __init__(self, conf):
        self.modelEvent = None
        self.bValue = "x"
        self.conf = conf

    def registerModelEvent(self, modelEvent):
        self.modelEvent = modelEvent

    #################################################
    def getBValue(self):
        return self.bValue

    def incButtonValue(self):
        self.bValue +="x"
        self.modelEvent.onButtonUpdated(self.bValue)
    ##################################################

    def getMacsDest(self):
        return self.conf.macsDest

    def getSicsDest(self):
        return self.conf.sicsDest

    def getSourceDest(self):
        return self.conf.sourceDest

    def getZipElements(self, withPath):
        zipElements =  [ "MacsConf_conf.zip" ]
        if not withPath:
            return zipElements
        else:
            zipElements2 = []
            for e in zipElements:
                zipElements2.append(f"{self.getSourceDest()}\\{e}")
            return zipElements2

    def getSourceElements(self, withPath):
        sourceElements =  [ "com.bull.mil.macs.conf.manager", "com.bull.mil.macs.confPims"  ]
        if not withPath:
            return zipElements
        else:
            sourceElements2 = []
            for e in sourceElements:
                sourceElements2.append(f"{self.getSourceDest()}\\{e}")
            return sourceElements2

    def getPathInDest(self, element):
        return f"ZE PATH IN DEST IS {element}"

    def replaceFile(self, element):
        ReplaceFileThread(self, element, 4).start()
