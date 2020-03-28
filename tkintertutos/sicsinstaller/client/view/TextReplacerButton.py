

# Button to remove, copy or unzip an element
from tkinter import Button


class TextReplacerButton(Button):
    # hintSearch : "macs" , "sics"
    # element : a file name
    def __init__(self, window, controller, text, hintSearch, element, clickFunction ):
        Button.__init__(self, window)
        self.configure(text=text, command=clickFunction)
        self.controller = controller
        self.hintSearch = hintSearch
        self.element = element
        self.refreshMMI()

    def refreshMMI(self):
        path = self.controller.getPath(self.element, self.hintSearch)
        if path != None:
            self.config(state='normal')
        else:
            self.config(state='disabled')






