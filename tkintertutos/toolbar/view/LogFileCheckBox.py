from tkinter import *

class LogFileCheckBox(Frame):
    def __init__(self, parent, title, controller):
        self.controller = controller
        Frame.__init__(self, parent)

        self.menubutton = Menubutton(self, text=title,
                                   indicatoron=True, borderwidth=1, relief="raised")
        self.menu = Menu(self.menubutton, tearoff=False)
        self.menubutton.configure(menu=self.menu)
        self.menubutton.pack(padx=10, pady=10)

        self.choices = {}
        #l = ["relay", "app", "azzer", "zeerr"]
        #for choice in ("Iron Man", "Superman", "Batman","Fartman","Babyman"):
        #for choice in l:
        #    self.choices[choice] = IntVar(value=0)
        #    self.menu.add_checkbutton(label=choice, variable=self.choices[choice],
        #                         onvalue=1, offvalue=0,
        #                         command=self.printValues)

    def onDirectoryReady(self, fileCategories):
        print ("fileCategories", fileCategories)
        # delete old menu
        for choice in self.choices:
            print("delete ", choice)
            self.menu.delete(0)

        for choice in fileCategories:
            self.choices[choice] = IntVar(value=0)
            self.menu.add_checkbutton(label=choice, variable=self.choices[choice],
                                 onvalue=1, offvalue=0,
                                 command=self.printValues)

        pass

    def printValues(self):
        print("================================")
        for name, var in self.choices.items():
            print (f"{name}: {var.get()}")
        print("================================")


