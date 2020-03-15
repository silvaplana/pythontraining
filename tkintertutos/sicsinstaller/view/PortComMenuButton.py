from tkinter import *

from tkinter import *


class PortComMenuButton(Menubutton):
    def __init__(self, window, controller, defaultValue):
        self.controller = controller
        Menubutton.__init__(self, window, text=defaultValue, relief=RAISED)

        self.choice = defaultValue

        self.mb_radmenu = Menu(self, tearoff=0)
        self.configure(menu=self.mb_radmenu)
        self.mb_radmenu.add_command(label='PIMS', underline=0, command=self.__comPims)
        self.mb_radmenu.add_command(label='COM1', underline=0, command=self.__com1)
        self.mb_radmenu.add_command(label='COM2', underline=0, command=self.__com2)
        self.mb_radmenu.add_command(label='COM3', underline=0, command=self.__com3)
        self.mb_radmenu.add_command(label='COM4', underline=0, command=self.__com4)
        self.mb_radmenu.add_command(label='COM5', underline=0, command=self.__com5)
        self.mb_radmenu.add_command(label='COM6', underline=0, command=self.__com6)


    def getChoice(self):
        return self.choice

    def __comPims(self):
        self.configure(text='PIMS')
        self.choice = 'PIMS'
    def __com1(self):
        self.configure(text='COM1')
        self.choice = 'COM1'

    def __com2(self):
        self.configure(text='COM2')
        self.choice = 'COM2'

    def __com3(self):
        self.configure(text='COM3')
        self.choice = 'COM3'

    def __com4(self):
        self.configure(text='COM4')
        self.choice = 'COM4'

    def __com5(self):
        self.configure(text='COM5')
        self.choice = 'COM5'

    def __com6(self):
        self.configure(text='COM6')
        self.choice = 'COM6'











