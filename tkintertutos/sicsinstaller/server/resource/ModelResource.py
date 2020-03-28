class ModelResource:
    def __init__(self, model):
        self.__m = model

    def registerModelEvent(self, modelEvent):
        self.__m.registerModelEvent(modelEvent)

    def getValue(self, key):
        return self.__m.getValue(key)

    def setValue(self, key, value):
        self.__m.setValue(key, value)

    def getPath(self, element, hintSearch="all"):
        return self.__m.getPath(element, hintSearch)

    def removeFileOrDir(self, path):
        self.__m.removeFileOrDir(path)

    def copyFileOrDir(self, srcPath, destDirPath):
        self.__m.copyFileOrDir(srcPath, destDirPath)

    def unzipFile(self, srcFilePath, destDirPath):
        self.__m.unzipFileOrDir(srcFilePath, destDirPath)

    def doesPathExist(self, path):
        return self.__m.doesPathExist(path)

    def onMacsLabelApply(self):
        self.__m.onMacsLabelApply()

    def onMacsComPortApply(self):
        self.__m.onMacsLabelApply()

    def onMacsChannelsConfApply(self):
        self.__m.onMacsChannelsConfApply()

    def getZipElements(self, withPath):
        return self.__m.getZipElements(withPath)

    def getSourceElements(self, withPath):
        return self.__m.getSourceElements(withPath)

