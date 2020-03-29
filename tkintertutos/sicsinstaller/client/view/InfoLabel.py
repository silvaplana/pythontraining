import threading
from time import sleep
from tkinter import *

class WaitingThread(threading.Thread):
    def __init__(self, infoLabel, durationS):
        threading.Thread.__init__(self)
        self.durationS = durationS
        self.infoLabel = infoLabel
        self.index = self.durationS * 10

    def restart(self):
        print ("restart")
        self.index = self.durationS * 10

    def run(self):
        while self.index>0:
            self.index =  self.index-1
            sleep(0.1)
        self.infoLabel.v.set("")
        print("     text configured :[]")



class InfoLabel(Label):

    def __init__(self, toolbar, text, controller):
        self.v = StringVar()
        self.v.set(text)
        Label.__init__(self, toolbar, textvariable=self.v)
        self.controller = controller
        self.waitingThread = None

    def setTexte(self, text):
        print("Entry to info label set text:", text)
        self.v.set(text)
        print("     text configured :[", text, "] configured")
        if self.waitingThread != None and self.waitingThread.is_alive():
            self.waitingThread.restart()
        else:
            self.waitingThread = WaitingThread(self, 2)
            self.waitingThread.start()





