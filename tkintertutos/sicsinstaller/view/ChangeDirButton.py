from tkinter import *


# Change dir button of source, macs dir or sics dir
class ChangeDirButton(Button):
    def __init__(self, window, controller, text,  element):
        Button.__init__(self, window)
        self.configure(text=text)
        self.controller = controller

    def onClick(self):
        pass




