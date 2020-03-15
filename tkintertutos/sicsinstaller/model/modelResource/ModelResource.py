class ModelResource:
    def __init__(self, model):
        self.__m = model

    def registerModelEvent(self, modelEvent):
        self.__m.registerModelEvent(modelEvent)

    def getMacsHierarchy(self):
        return self.__m.getMacsHierarchy()

    def getSicsHierarchy(self):
        return self.__m.getSicsHierarchy()

    def getMacsDest(self):
        return self.__m.getMacsDest()

    def getSicsDest(self):
        return self.__m.getSicsDest()

    def getSourceDest(self):
        return self.__m.getSourceDest()

    def getMacsData(self):
        return self.__m.getMacsData()

    def getSicsData(self):
        return self.__m.getSicsData()

    def getMacsLabel(self):
        return self.__m.getMacsLabel()

    def getMacsComPort(self):
        return self.__m.getMacsComPort()

    def getMacsChannelsConf(self):
        return self.__m.getMacsChannelsConf()

    def getZipElements(self, withPath):
        return self.__m.getZipElements(withPath)

    def getSourceElements(self, withPath):
        return self.__m.getSourceElements(withPath)

    def getPathInDest(self, element):
        return self.__m.getPathInDest(element)

    def replaceFile(self, element):
        print("entry in replaceFile, element=", element)
        self.__m.replaceFile(element)
