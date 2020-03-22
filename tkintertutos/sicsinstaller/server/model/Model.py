import os
import threading
from time import sleep

from pythontraining.tkintertutos.sicsinstaller.server.model.Persistence import Persistence
from pythontraining.tkintertutos.utilities.FileOp import FileOp


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
        self.fileOp = FileOp()
        self.conf = conf
        self.persistence = Persistence(self)
        # vals are stored in persistence
        # keys are : macsHierarchy, sicsHierarchy, sourceDir, macsLabel, macsComPort, MacsChannelsConf
        self.vals = {}
        self.__loadConf()

    def registerModelEvent(self, modelEvent):
        self.modelEvent = modelEvent

    def getValue(self, key):
            if key in self.vals.keys():
                return self.vals[key]
            else:
                return f"not found {key}"

    def setValue(self, key, value):
            if key in self.vals.keys():
                self.vals[key] = value
                self.persistence.saveAll()
                self.modelEvent.onValueUpdated(key, value)
            else:
                return  print ("not found", key, ": impossible to set value")

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
        sourceElements =  [ "com.bull.mil.macs.conf.manager.cfg", "com.bull.mil.macs.confPims.xml"  ]
        if not withPath:
            return sourceElements
        else:
            sourceElements2 = []
            for e in sourceElements:
                sourceElements2.append(f"{self.getSourceDest()}\\{e}")
            return sourceElements2

    def onMacsLabelApply(self):
        pass

    def onMacsComPortApply(self):
        pass

    def onMacsChannelsConfApply(self):
        pass

    # get path in macs hierarchy (option="macs")  or sics hierarchy  (option="sics") or both hierarchy (option="all")
    # hintSearch : "macs" , "sics", or "all"
    # element : a directory or a file name , can be preceeded by path.  There are special words : #macs , #sics , the root for macs and sics directories : below is data, below is...
    def getPath(self, element, hintSearch="all"):

        strElement = element

        # replace #macs  and #sics by their path
        if "#macs" in strElement:
            if not self.__getMacsDir() == None:
                strElement = strElement.replace("#macs", self.__getMacsDir())
            else:
                return None

        if "#sics" in strElement:
            if not self.__getSicsDir() == None:
                strElement = strElement.replace("#sics", self.__getSicsDir())
            else:
                return None

        strTmp = ""
        pathFound = None

        if (hintSearch == "macs" or hintSearch == "all") and "macsHierarchy" in  self.vals:
            pathFound = self.__getPathThatEndsWith(self.vals["macsHierarchy"], strElement)
            if pathFound != None:
                return pathFound

        if (hintSearch == "sics" or hintSearch == "all") and "sicsHierarchy" in  self.vals:
            pathFound = self.__getPathThatEndsWith(self.vals["sicsHierarchy"], strElement)
            if pathFound != None:
                return pathFound
        return None

    def removeFileOrDir(self, path):
        self.fileOp.removeFileOrDir(path)
        self.modelEvent.onInfoLabelUpdate(f"element {path} removed")


    ## private methods

    def __loadConf(self):
        self.vals = self.persistence.loadAll()

    #def __replaceFile(self, element):
    #    ReplaceFileThread(self, element, 4).start()

    def __getMacsDir(self):
        pattern = "/bin/macs-sics-server-runtime.cmd"

        pathFound = self.__getPathThatEndsWith (self.vals["macsHierarchy"], pattern)
        if pathFound == None:
            return None
        pathFound = pathFound.replace(pattern, "")
        return pathFound

    def __getSicsDir(self):
        pattern = "/factory/fr.dga.sics.profile.cfg"
        pathFound = self.__getPathThatEndsWith(self.vals["sicsHierarchy"], pattern)
        if pathFound == None:
            return None
        pathFound = pathFound.replace(pattern, "")
        return pathFound

    def __getPathThatEndsWith (self, startPath, endsWithStr):
        for root, dirs, files in os.walk(startPath):
            for name in files:
                strTmp = os.path.join(root, name)
                strTmp = strTmp.replace("\\", "/")
                if strTmp.endswith(endsWithStr):
                    return strTmp
            for name in dirs:
                strTmp = os.path.join(root, name)
                strTmp =  strTmp.replace("\\", "/")
                if strTmp.endswith(endsWithStr):
                    return strTmp
        return None