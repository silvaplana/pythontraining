from tkinter import *


# Button to remove, copy or unzip an element
class RcuButton(Button):
    def __init__(self, window, controller, text,  operation, element):
        Button.__init__(self, window)
        self.configure(text=text)
        self.controller = controller

    def onClick(self):
        pass





