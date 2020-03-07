
class Controller():

    def __init__(self, model):
        self.model = model

    def setWidgets (self, menuApp, infoLabel, fileSelectorCB, fileMergerCB, textWidget ):
        self.menuApp = menuApp
        self.infoLabel = infoLabel
        self.fileSelectorCB = fileSelectorCB
        self.fileMergerCB = fileMergerCB
        self.textWidget = textWidget


    # FROM MMI TO MODEL

    def onClickLoadFile(self, filepath):
        if "." in filepath:
            #text = self.model.loadFile (filepath)
            #self.textWidget.displayFile(text)
            self.model.loadDirectory(filepath)
        else:
            self.model.loadDirectory(filepath)

    # FROM

    def onLoadFileStepCompletedEvent(self, message, isFinished):
        if isFinished == True:
            self.infoLabel.setText("")

    def onLoadDirectoryStepCompletedEvent(self, message, isFinished, fileCategories):
        if isFinished == True:
            self.infoLabel.setText("")
            self.fileMergerCB.onDirectoryReady(fileCategories)
            self.fileSelectorCB.onDirectoryReady(fileCategories)
        else:
            self.infoLabel.setText(message)



