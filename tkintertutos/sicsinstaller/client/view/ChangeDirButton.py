from tkinter import *


# Change dir button of source, macs dir or sics dir
from tkinter import filedialog


class ChangeDirButton(Button):
    def __init__(self, window, controller, text , element):
        Button.__init__(self, window, command=self.onClick)
        self.configure(text=text)
        self.controller = controller
        self.element = element

    def onClick(self):
        newDirectory = filedialog.askdirectory()
        self.controller.onNewValueSelection(self.element, newDirectory)




