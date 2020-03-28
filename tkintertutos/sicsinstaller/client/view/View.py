from threading import Thread, Event
from tkinter import Label, StringVar, Button
from tkinter.ttk import Entry

from pythontraining.tkintertutos.sicsinstaller.client.view.ChangeDirButton import ChangeDirButton
from pythontraining.tkintertutos.sicsinstaller.client.view.ChannelsConfMenuButton import ChannelsConfMenuButton
from pythontraining.tkintertutos.sicsinstaller.client.view.InfoLabel import InfoLabel
from pythontraining.tkintertutos.sicsinstaller.client.view.PortComMenuButton import PortComMenuButton
from pythontraining.tkintertutos.sicsinstaller.client.view.RcuButton import RcuButton
from pythontraining.tkintertutos.sicsinstaller.client.view.TextReplacerButton import TextReplacerButton
from pythontraining.tkintertutos.sicsinstaller.server.event.ModelEvent import ModelEvent


# refresh mmi every 5 seconds
class RefreshMMiThread(Thread):
    def __init__(self, stopEvent, view):
        Thread.__init__(self)
        self.stopped = stopEvent
        self.view = view

    def run(self):
        while not self.stopped.wait(5):
            print("Refresh MMI")
            self.view.refreshMMI()





class View(ModelEvent):
    def __init__(self, window, controller):
        self.window = window
        self.controller = controller
        ModelEvent.__init__(self)
        self.rcuButons = []
        self.textReplacerButons = []
        self.initMMI()

        #start thread that refresh periodically mmi
        self.stopFlag = Event()
        self.refreshMMiThread = RefreshMMiThread(self.stopFlag, self)
        self.refreshMMiThread.start()
        # this will stop the timer : self.stopFlag.set()


    def initMMI(self):

        currentLine = 0

        #Ligne 1 : info label
        currentLine+=1
        self.infoLabel = InfoLabel(self.window, "", self.controller)
        self.infoLabel.grid(row=currentLine, column=2)

        # Ligne 1 prime : vide
        currentLine += 1
        Label(self.window, text="Source and destination directories:", borderwidth=5, font='Helvetica 12 bold').grid(
            row=currentLine, column=2)

        # Ligne 2 : source
        currentLine += 1
        Label(self.window, text='Source directory:', borderwidth=5).grid(row=currentLine, column=1)
        self.sourceDir = StringVar()
        self.sourceDir.set(self.controller.getValue("sourceDir"))
        Label(self.window, textvariable=self.sourceDir, borderwidth=5).grid(row=currentLine, column=2)
        ChangeDirButton(self.window, self.controller, "Change", "sourceDir").grid(row=currentLine, column=3)

        # Ligne 3 : macs Hierarchy
        currentLine += 1
        Label(self.window, text='Macs hierarchy:', borderwidth=5).grid(row=currentLine, column=1)
        self.macsHierarchy = StringVar()
        self.macsHierarchy.set(self.controller.getValue("macsHierarchy"))
        Label(self.window, textvariable=self.macsHierarchy, borderwidth=5).grid(row=currentLine, column=2)
        ChangeDirButton(self.window, self.controller, "Change", "macsHierarchy").grid(row=currentLine, column=3)

        # Ligne 4 : sics
        currentLine += 1
        Label(self.window, text='Sics hierarchy:', borderwidth=5).grid(row=currentLine, column=1)
        self.sicsHierarchy = StringVar()
        self.sicsHierarchy.set(self.controller.getValue("sicsHierarchy"))
        Label(self.window, textvariable=self.sicsHierarchy, borderwidth=5).grid(row=currentLine, column=2)
        ChangeDirButton(self.window, self.controller, "Change", "sicsHierarchy").grid(row=currentLine, column=3)

        # Ligne 5 : vide
        currentLine += 1
        Label(self.window, text="Remove:", borderwidth=5, font='Helvetica 12 bold').grid(
            row=currentLine, column=2)

        # Ligne 6 : remove macs data
        currentLine += 1
        self.rcuButons.append(RcuButton(self.window, self.controller, "Remove macs directory", "REMOVE", "macs", "#macs"))
        self.rcuButons[-1].grid(row=currentLine, column=1)
        self.rcuButons.append(RcuButton(self.window, self.controller, "Remove macs data directory", "REMOVE", "macs", "#macs/data"))
        self.rcuButons[-1].grid(row=currentLine, column=2)

        # Ligne 7 : remove sics data
        currentLine += 1
        self.rcuButons.append(RcuButton(self.window, self.controller, "Remove sics  directory", "REMOVE", "sics", "#sics"))
        self.rcuButons[-1].grid(row=currentLine, column=1)
        self.rcuButons.append(RcuButton(self.window, self.controller, "Remove sics data directory", "REMOVE", "sics", "#sics/data"))
        self.rcuButons[-1].grid(row=currentLine, column=2)

        # Ligne 7 prime : vide
        currentLine += 1
        Label(self.window, text="Copy , unzip:", borderwidth=5, font='Helvetica 12 bold').grid(
            row=currentLine, column=2)

        # Ligne i : elements a dezipper
        sourceZipElts = self.controller.getZipElements(False)
        for el in range(len(sourceZipElts)):
            currentLine += 1
            self.rcuButons.append(RcuButton(self.window, self.controller, f"Remove remote {sourceZipElts[el]}", "REMOVE", "all", sourceZipElts[el]))
            self.rcuButons[-1].grid(row=currentLine, column=1)
            self.rcuButons.append(RcuButton(self.window, self.controller, f"Copy {sourceZipElts[el]}", "COPY", "all", sourceZipElts[el]))
            self.rcuButons[-1].grid(row=currentLine, column=2)
            self.rcuButons.append(RcuButton(self.window, self.controller, f"Unzip remote", "UNZIP", "all", sourceZipElts[el]))
            self.rcuButons[-1].grid(row=currentLine, column=3)

        # Ligne j : elements a copier
        sourceElts = self.controller.getSourceElements(False)
        for el in range(len(sourceElts)):
            currentLine += 1
            self.rcuButons.append(RcuButton(self.window, self.controller, f"Remove remote {sourceElts[el]}", "REMOVE", "all", sourceElts[el]))
            self.rcuButons[-1].grid(row=currentLine, column=1)
            self.rcuButons.append(RcuButton(self.window, self.controller, f"Copy {sourceElts[el]}", "COPY", "all", sourceElts[el]))
            self.rcuButons[-1].grid(row=currentLine, column=2)

        # Ligne k : vide
        currentLine += 1
        Label(self.window, text="Change values:", borderwidth=5, font='Helvetica 12 bold').grid(
            row=currentLine, column=2)

        # Ligne l : macs label button change
        currentLine += 1
        Label(self.window, text='Label:', borderwidth=5).grid(row=currentLine, column=1)
        self.macsLabel = StringVar()
        self.macsLabel.set(self.controller.getValue("macsLabel"))
        self.macsLabel.trace("w", lambda name, index, mode, sv=self.macsLabel: self.onMacsLabelSelected(self.macsLabel.get()))
        self.labelEntry = Entry(self.window, textvariable=self.macsLabel, width=4).grid(row=currentLine, column=2)
        self.textReplacerButons.append(TextReplacerButton(self.window, self.controller, "Change", "sics", "fr.dga.sics.profile.cfg", self.onMacsLabelApply))
        self.textReplacerButons[-1].grid(row=currentLine, column=3)

        # Ligne m : definition PORT COM
        currentLine += 1
        Label(self.window, text='Com port:', borderwidth=5).grid(row=currentLine, column=1)
        self.portComButton = PortComMenuButton(self.window, self.controller, self.controller.getValue("macsComPort")).grid(row=currentLine, column=2)
        self.textReplacerButons.append(TextReplacerButton(self.window, self.controller, "Change", "macs","com.bull.mil.macs.conf.xml", self.onMacsComPortApply))
        self.textReplacerButons[-1].grid(row=currentLine, column=3)

        # Ligne n : channels configuratio Configuration change
        currentLine += 1
        Label(self.window, text='Channels configuration:', borderwidth=5).grid(row=currentLine, column=1)
        self.channelsConfMenuButton = ChannelsConfMenuButton(self.window, self.controller, self.controller.getValue("macsChannelsConf")).grid(row=currentLine, column=2)
        self.textReplacerButons.append(TextReplacerButton(self.window, self.controller, "Change", "macs", "com.bull.mil.macs.conf.xml", self.channelsConfMenuButton))
        self.textReplacerButons[-1].grid(row=currentLine, column=3)

        # Ligne o : vide
        currentLine += 1
        Label(self.window, text="", borderwidth=5, font='Helvetica 12 bold').grid(
            row=currentLine, column=2)


    # refresh MMI
    def refreshMMI(self):
        for btn in self.rcuButons:
            btn.refreshMMI()
        for btn in self.textReplacerButons:
            btn.refreshMMI()



    # On click actions

    # when entry widget is edited
    def onMacsLabelSelected(self, sv):
        self.controller.onNewValueSelection("macsLabel", sv)

    # when file modification is asked
    def onMacsLabelApply(self):
        path = self.controller.getPath("fr.dga.sics.profile.cfg", "sics")
        if path == None:
            print("Impossible to replace text in", self.element, "path cannot be found")
        self.controller.onMacsLabelApply()

    # when file modification is asked
    def onMacsComPortApply(self):
        path = self.controller.getPath("com.bull.mil.macs.conf.xml", "macs")
        if path == None:
            print("Impossible to replace text in", self.element, "path cannot be found")
        self.controller.onMacsComPortApply()

    # when file modification is asked
    def onMacsChannelsConfApply(self):
        path = self.controller.getPath("com.bull.mil.macs.conf.xml", "macs")
        if path == None:
            print("Impossible to replace text in", self.element, "path cannot be found")
        self.controller.onMacsChannelsConfApply()

    #End on click actions




    # ModelEvent implementations


    def onValueUpdated(self, key, value):
        if key == "macsHierarchy":
            self.macsHierarchy.set(value)
        elif key == "sicsHierarchy":
            self.sicsHierarchy.set(value)
        elif key == "sourceDir":
            self.sourceDir.set(value)
        elif key == "macsLabel":
            self.macsLabel.set(value)
        #elif key == "macsComPort":
        #    self.portComButton.configure(text=value)
        #elif key == "macsChannelsConf":
        #    self.channelsConfMenuButton.configure(text=value)

    def onInfoLabelUpdate(self, value):
        print ("onInfoLabelUpdate entry", value)
        self.infoLabel.setTexte(value)

    # operation is "created", "removed", "unzipped"
    def onFileOrDirUpdated(self, path, operation):
        self.infoLabel.setTexte(f"{path} has been {operation}")
        self.refreshMMI()



    # end of ModelEvent implementations