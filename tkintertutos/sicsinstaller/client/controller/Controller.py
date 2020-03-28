class Controller():

    def __init__(self, modelResource):
        self.model = modelResource

    def getValue(self, key):
        return self.model.getValue(key)

    def setValue(self, key, value):
        self.model.setValue(key, value)

    def onNewValueSelection(self,key, value):
        self.model.setValue(key, value)

    def getPath(self, element, hintSearch="all"):
        return self.model.getPath(element, hintSearch)

    def removeFileOrDir(self, path):
        self.model.removeFileOrDir(path)

    def copyFileOrDir(self, srcPath, destDirPath):
        self.model.copyFileOrDir(srcPath, destDirPath)

    def unzipFile(self, srcFilePath, destDirPath):
        self.model.unzipFileOrDir(srcFilePath, destDirPath)

    def doesPathExist(self, path):
        return self.model.doesPathExist(path)

    def getZipElements(self, withPath):
        return self.model.getZipElements(withPath)

    def getSourceElements(self, withPath):
        return self.model.getSourceElements(withPath)

    # change buttons clicked
    def onMacsLabelApply(self):
        self.model.onMacsLabelApply()
    def onMacsComPortApply(self):
        self.model.onMacsComPortApply()
    def onMacsChannelsConfApply(self):
        self.model.onMacsChannelsConfApply()





