#! /usr/bin/python
# File: ToolbarEx.py

from tkinter import *

import PIL
from PIL import Image, ImageTk

class App():
    def __init__(self):
        self.root = Tk()

        # Create the toolbar as a frame
        self.toolbar = Frame(self.root, borderwidth=2, relief='raised')

        # Load all the images first as PNGs and use ImageTk to convert
        # them to usable Tkinter images.
        #self.img1 = Image.open('NewIcon.png')
        self.img1 = PIL.Image.open("NewIcon.png")
        self.useImg1 = PIL.ImageTk.PhotoImage(self.img1)
        self.img2 = Image.open('LoadIcon.png')
        self.useImg2 = ImageTk.PhotoImage(self.img2)
        self.img3 = Image.open('SaveIcon.png')
        self.useImg3 = ImageTk.PhotoImage(self.img3)
        self.img4 = Image.open('QuitButton.png')
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

        # Add the toolbar
        self.toolbar.pack(side=TOP, fill=X)

        # Set up a Text box and scroll bar.
        self.scrollbar = Scrollbar(self.root)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.text = Text(self.root)
        self.text.pack()

        self.text.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.text.yview)
        

    def callback(self):
        print ("A button was pressed")

if __name__ == "__main__":
    a = App()
    a.root.mainloop()

