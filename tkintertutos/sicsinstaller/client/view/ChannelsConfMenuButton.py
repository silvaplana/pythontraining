from tkinter import *

from tkinter import *


class ChannelsConfMenuButton(Menubutton):
    def __init__(self, window, controller, defaultValue):
        self.controller = controller
        self.choice = defaultValue

        Menubutton.__init__(self, window, text=defaultValue, relief=RAISED)
        self.mb_radmenu = Menu(self, tearoff=0)
        self.configure(menu=self.mb_radmenu)
        self.mb_radmenu.add_command(label='0,1', underline=0, command=self.__conf01)
        self.mb_radmenu.add_command(label='3,4', underline=0, command=self.__conf34)
        self.mb_radmenu.add_command(label='5,6', underline=0, command=self.__conf56)

    def getChoice(self):
        return self.choice

    def __conf01(self):
        self.configure(text='0,1')
        self.choice = '0,1'

    def __conf34(self):
        self.configure(text='3,4')
        self.choice = '3,4'

    def __conf56(self):
        self.configure(text='5,6')
        self.choice = '5,6'

