
#class OnClickButtonThreadThread(threading.Thread):
#    def __init__(self, model):
#        threading.Thread.__init__(self)
#        self.model = model
#    def run (self):
#        self.model.incButtonValue()


class Controller():

    def __init__(self, modelResource):
        self.model = modelResource

    def onNewValueSelection(self,key, value):
        self.model.setValue(key, value)

    def getPath(self, element, hintSearch="all"):
        return self.model.getPath(element, hintSearch)

    def onRcuButtonClick(self, operation, element):
        print ("controller on ", operation, element)

    # change button clicked
    def onMacsLabelApply(self):
        self.model.onMacsLabelApply()

    # change button clicked
    def onMacsComPortApply(self):
        self.model.onMacsComPortApply()

    # change button clicked
    def onMacsChannelsConfApply(self):
        self.model.onMacsChannelsConfApply()





