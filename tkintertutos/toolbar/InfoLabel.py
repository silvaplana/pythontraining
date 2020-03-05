from tkinter import *

class InfoLabel(Label):
    def __init__(self, toolbar, text):
        self.v = StringVar()
        self.v.set(text)
        Label.__init__(self, toolbar, textvariable=self.v)


    def setText(self, text):
        self.v.set(text)
        print ("self.v=", self.v)


