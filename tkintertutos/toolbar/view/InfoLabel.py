from tkinter import *

class InfoLabel(Label):
    def __init__(self, toolbar, text, controller):
        self.v = StringVar()
        self.v.set(text)
        #Label.__init__(self, toolbar, textvariable=self.v)
        Label.__init__(self, toolbar)
        self.configure(text=text)
        self.controller = controller

    def setText(self, text):
        #self.v.set(text)
        self.configure(text=text)
        print ("info label updated :", text)


