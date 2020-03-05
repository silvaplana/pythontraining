from tkinter import *

class LogFileCheckBox(Frame):
    def __init__(self, parent, title):
        Frame.__init__(self, parent)

        menubutton = Menubutton(self, text=title,
                                   indicatoron=True, borderwidth=1, relief="raised")
        menu = Menu(menubutton, tearoff=False)
        menubutton.configure(menu=menu)
        menubutton.pack(padx=10, pady=10)

        self.choices = {}
        l = ["relay", "app", "azzer", "zeerr"]
        #for choice in ("Iron Man", "Superman", "Batman","Fartman","Babyman"):
        for choice in l:
            self.choices[choice] = IntVar(value=0)
            menu.add_checkbutton(label=choice, variable=self.choices[choice],
                                 onvalue=1, offvalue=0,
                                 command=self.printValues)
    def printValues(self):
        print("================================")
        for name, var in self.choices.items():
            print (f"{name}: {var.get()}")
        print("================================")


