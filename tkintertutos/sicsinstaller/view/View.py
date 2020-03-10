from tkinter import Label, StringVar, Button

from tkintertutos.sicsinstaller.model.ModelEvent import ModelEvent


class View(ModelEvent):
    def __init__(self, window, controller, model):
        self.window = window
        self.controller = controller
        self.model = model
        ModelEvent.__init__(self)
        self.initMMI()


    def initMMI(self):
        self.bValue = StringVar()
        self.bValue.set(self.model.getBValue())
        button = Button(self.window, textvariable=self.bValue, command=self.onButtonClick)
        button.pack()

    # MMI actions

    def onButtonClick(self):
        self.controller.onClickOnButton()

    # MMI actions end

    # model event implementations
    def onButtonUpdated(self, value):
        self.bValue.set(value)
        print("onButtonUpdated value", value)

    def onInfoLabelUpdate(self, value):
        pass


    # end of model event implementations