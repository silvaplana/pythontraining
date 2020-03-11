from tkinter import *

import PIL
from PIL import Image, ImageTk

from tkintertutos.toolbar.controller.Controller import Controller
from tkintertutos.toolbar.model.Model import Model
from tkintertutos.toolbar.view.InfoLabel import InfoLabel
from tkintertutos.toolbar.view.LogFileCheckBox import LogFileCheckBox
from tkintertutos.toolbar.view.MenuApp import MenuApp
from tkintertutos.toolbar.view.TextWidget import TextWidget


class App():
    def __init__(self, master=None):
        self.root = Tk()
        self.model = Model()
        self.controller = Controller(self.model)
        self.model.setController(self.controller)
        self.toolbar = None
        self.initMMi()

    def initMMi (self, master=None):
        # Create the toolbar as a frame
        self.toolbar = Frame(self.root,  borderwidth=2, relief='raised')

        self.menuBar = MenuApp(self.root, self.controller)

        # Load all the images first as PNGs and use ImageTk to convert
        # them to usable Tkinter images.
        #self.img1 = Image.open('NewIcon.png')
        self.img1 = PIL.Image.open("view/NewIcon.png")
        self.useImg1 = PIL.ImageTk.PhotoImage(self.img1)
        self.img2 = Image.open('view/LoadIcon.png')
        self.useImg2 = ImageTk.PhotoImage(self.img2)
        self.img3 = Image.open('view/SaveIcon.png')
        self.useImg3 = ImageTk.PhotoImage(self.img3)
        self.img4 = Image.open('view/QuitButton.png')
        self.useImg4 = ImageTk.PhotoImage(self.img4)

        # Set up all the buttons for use on the toolbars.
        newBtn = Button(self.toolbar, image=self.useImg1, command=self.callback)
        newBtn.pack(side=LEFT, fill=X)

        loadBtn = Button(self.toolbar, image=self.useImg2, command=self.callback)
        loadBtn.pack(side=LEFT, fill=X)

        saveBtn = Button(self.toolbar, image=self.useImg3, command=self.callback)
        saveBtn.pack(side=LEFT, fill=X)

        quitBtn = Button(self.toolbar, image=self.useImg4, command=self.callback)
        quitBtn.pack(side=LEFT, fill=X)


        self.fileSelector = LogFileCheckBox(self.toolbar, "File selector", self.controller)
        self.fileSelector.pack(side=LEFT, fill=X)
        self.fileMerger = LogFileCheckBox(self.toolbar, "File Merger",  self.controller)
        self.fileMerger.pack(side=LEFT, fill=X)

        self.infoLabel = InfoLabel(self.toolbar, "", self.controller)

        self.infoLabel.pack(side=LEFT, fill=X)



        # Add the toolbar
        self.toolbar.pack(side=TOP, fill=X)


        # Set up a Text box and scroll bar.
        self.scrollbar = Scrollbar(self.root)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.text = TextWidget(self.root, self.controller)
        self.text.pack(expand=True, fill=BOTH)

        self.text.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.text.yview)

        #self.controller.setWidgets(self.menuBar, self.infoLabel, self.fileSelector, self.fileMerger, self.text)


    def callback(self):
        print ("A button was pressed")



if __name__ == "__main__":
    print("==================== begin ======================")
    a = App()
    a.root.mainloop()

