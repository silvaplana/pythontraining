from tkinter import *

class TextWidget(Text):
    def __init__(self , root, controller ):
        self.controller = controller
        Text.__init__(self, root)

    def displayFile(self, text):
        print ("text to be displayed", text)

        self.insert(END, text)



