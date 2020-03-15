
#class OnClickButtonThreadThread(threading.Thread):
#    def __init__(self, model):
#        threading.Thread.__init__(self)
#        self.model = model
#    def run (self):
#        self.model.incButtonValue()


class Controller():

    def __init__(self, modelResource):
        self.model = modelResource

    def onClickOnButton(self):
        self.model.incButtonValue()



