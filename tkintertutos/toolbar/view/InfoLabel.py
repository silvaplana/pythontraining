import threading
from time import sleep
from tkinter import *

class WaitingThread(threading.Thread):
    def __init__(self, infoLabel, durationS):
        threading.Thread.__init__(self)
        self.durationS = durationS
        self.infoLabel = infoLabel

    def run(self):
        sleep(self.durationS)
        self.infoLabel.configure(text="")



class InfoLabel(Label):

    def __init__(self, toolbar, text, controller):
        self.v = StringVar()
        self.v.set(text)
        Label.__init__(self, toolbar)
        self.configure(text=text)
        self.controller = controller

    def setTexte(self, text):
        self.configure(text=text)
        print ("info label updated :", text)
        t = WaitingThread(self, 1)
        t.start()





