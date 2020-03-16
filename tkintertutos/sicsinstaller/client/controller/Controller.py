
#class OnClickButtonThreadThread(threading.Thread):
#    def __init__(self, model):
#        threading.Thread.__init__(self)
#        self.model = model
#    def run (self):
#        self.model.incButtonValue()


class Controller():

    def __init__(self, modelResource):
        self.model = modelResource

    def onRcuButtonClick(self, operation, element):
        print ("controller on ", operation, element)


    def onNewDirectoryClick(self,element, newDirectory):
        if element == "#macsHierarchy":
            self.model.setMacsHierarchy(newDirectory)
        elif element == "#sicsHierarchy":
            self.model.setSicsHierarchy(newDirectory)
        elif element == "#sourceDest":
            self.model.setSourceDest(newDirectory)


