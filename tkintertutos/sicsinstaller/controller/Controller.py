
#class OnClickButtonThreadThread(threading.Thread):
#    def __init__(self, model):
#        threading.Thread.__init__(self)
#        self.model = model
#    def run (self):
#        self.model.incButtonValue()


class Controller():

    def __init__(self, model):
        self.model = model

    def onRcuButtonClick(self, operation, element):
        print ("controller on ", operation, element)



