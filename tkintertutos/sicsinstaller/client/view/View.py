from tkinter import Label, StringVar, Button
from tkinter.ttk import Entry

from pythontraining.tkintertutos.sicsinstaller.client.view.ChangeDirButton import ChangeDirButton
from pythontraining.tkintertutos.sicsinstaller.client.view.ChannelsConfMenuButton import ChannelsConfMenuButton
from pythontraining.tkintertutos.sicsinstaller.client.view.PortComMenuButton import PortComMenuButton
from pythontraining.tkintertutos.sicsinstaller.client.view.RcuButton import RcuButton
from pythontraining.tkintertutos.sicsinstaller.server.event.ModelEvent import ModelEvent
from pythontraining.tkintertutos.toolbar.view.InfoLabel import InfoLabel


class View(ModelEvent):
    def __init__(self, window, controller, modelResource):
        self.window = window
        self.controller = controller
        self.model = modelResource
        ModelEvent.__init__(self)
        self.rcuButons = []
        self.initMMI()

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
        self.sourceDir.set(self.model.getValue("sourceDir"))
        Label(self.window, textvariable=self.sourceDir, borderwidth=5).grid(row=currentLine, column=2)
        ChangeDirButton(self.window, self.controller, "Change", "sourceDir").grid(row=currentLine, column=3)

        # Ligne 3 : macs Hierarchy
        currentLine += 1
        Label(self.window, text='Macs hierarchy:', borderwidth=5).grid(row=currentLine, column=1)
        self.macsHierarchy = StringVar()
        self.macsHierarchy.set(self.model.getValue("macsHierarchy"))
        Label(self.window, textvariable=self.macsHierarchy, borderwidth=5).grid(row=currentLine, column=2)
        ChangeDirButton(self.window, self.controller, "Change", "macsHierarchy").grid(row=currentLine, column=3)

        # Ligne 4 : sics
        currentLine += 1
        Label(self.window, text='Sics hierarchy:', borderwidth=5).grid(row=currentLine, column=1)
        self.sicsHierarchy = StringVar()
        self.sicsHierarchy.set(self.model.getValue("sicsHierarchy"))
        Label(self.window, textvariable=self.sicsHierarchy, borderwidth=5).grid(row=currentLine, column=2)
        ChangeDirButton(self.window, self.controller, "Change", "sicsHierarchy").grid(row=currentLine, column=3)

        # Ligne 5 : vide
        currentLine += 1
        Label(self.window, text="Remove:", borderwidth=5, font='Helvetica 12 bold').grid(
            row=currentLine, column=2)

        # Ligne 6 : remove macs data
        currentLine += 1
        thebt = RcuButton(self.window, self.controller, "Remove macs directory", "REMOVE", "macs", "#macs").grid(row=currentLine, column=1)
        self.rcuButons.append(thebt)
        self.rcuButons.append(RcuButton(self.window, self.controller, "Remove macs data directory", "REMOVE", "macs", "#macs/data").grid(row=currentLine, column=2))

        # Ligne 7 : remove sics data
        currentLine += 1
        self.rcuButons.append(RcuButton(self.window, self.controller, "Remove sics  directory", "REMOVE", "sics", "#sics").grid(row=currentLine, column=1))
        self.rcuButons.append(RcuButton(self.window, self.controller, "Remove sics data directory", "REMOVE", "sics", "#sics/data").grid(row=currentLine, column=2))

        # Ligne 7 prime : vide
        currentLine += 1
        Label(self.window, text="Copy , unzip:", borderwidth=5, font='Helvetica 12 bold').grid(
            row=currentLine, column=2)

        # Ligne i : elements a dezipper
        sourceZipElts = self.model.getZipElements(False)
        for el in range(len(sourceZipElts)):
            currentLine += 1
            self.rcuButons.append(RcuButton(self.window, self.controller, f"Remove remote {sourceZipElts[el]}", "REMOVE", "all", sourceZipElts[el]).grid(row=currentLine, column=1))
            self.rcuButons.append(RcuButton(self.window, self.controller, f"Copy {sourceZipElts[el]}", "COPY", "all", sourceZipElts[el]).grid(row=currentLine, column=2))
            self.rcuButons.append(RcuButton(self.window, self.controller, f"Unzip remote", "UNZIP", "all", sourceZipElts[el]).grid(row=currentLine, column=3))

        # Ligne j : elements a copier
        sourceElts = self.model.getSourceElements(False)
        for el in range(len(sourceElts)):
            currentLine += 1
            self.rcuButons.append(RcuButton(self.window, self.controller, f"Remove remote {sourceElts[el]}", "REMOVE", "all", sourceElts[el]).grid(row=currentLine, column=1))
            self.rcuButons.append(RcuButton(self.window, self.controller, f"Copy {sourceElts[el]}", "COPY", "all", sourceElts[el]).grid(row=currentLine, column=2))

        # Ligne k : vide
        currentLine += 1
        Label(self.window, text="Change values:", borderwidth=5, font='Helvetica 12 bold').grid(
            row=currentLine, column=2)

        # Ligne l : definition label
        currentLine += 1
        Label(self.window, text='Label:', borderwidth=5).grid(row=currentLine, column=1)
        self.macsLabel = StringVar()
        self.macsLabel.set(self.model.getValue("macsLabel"))
        self.macsLabel.trace("w", lambda name, index, mode, sv=self.macsLabel: self.onMacsLabelSelected(self.macsLabel.get()))
        Entry(self.window, textvariable=self.macsLabel, width=4).grid(row=currentLine, column=2)
        Button(self.window, text="Change", command=self.onMacsLabelApply).grid(row=currentLine, column=3)

        # Ligne m : definition PORT COM
        currentLine += 1
        Label(self.window, text='Com port:', borderwidth=5).grid(row=currentLine, column=1)
        self.portComButton = PortComMenuButton(self.window, self.controller, self.model.getValue("macsComPort")).grid(row=currentLine, column=2)
        Button(self.window, text="Change", command=self.onMacsComPortApply).grid(row=currentLine, column=3)

        # Ligne n : Configuration change
        currentLine += 1
        Label(self.window, text='Channels configuration:', borderwidth=5).grid(row=currentLine, column=1)
        self.channelsConfMenuButton = ChannelsConfMenuButton(self.window, self.controller, self.model.getValue("macsChannelsConf")).grid(row=currentLine, column=2)
        Button(self.window, text="Change", command=self.onMacsChannelsConfApply).grid(row=currentLine, column=3)

        # Ligne o : vide
        currentLine += 1
        Label(self.window, text="", borderwidth=5, font='Helvetica 12 bold').grid(
            row=currentLine, column=2)


    # refresh MMI
    def refreshMMI(self):
        for btn in self.rcuButons:
            btn.refreshMMI()

    # On click actions

    # when entry widget is edited
    def onMacsLabelSelected(self, sv):
        self.controller.onNewValueSelection("macsLabel", sv)

    # when file modification is asked
    def onMacsLabelApply(self):
        self.controller.onMacsLabelApply()

    # when file modification is asked
    def onMacsComPortApply(self):
        self.controller.onMacsComPortApply()

    # when file modification is asked
    def onMacsChannelsConfApply(self):
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
        print ("value is", value)
        self.infoLabel.setTexte(value)



    # end of ModelEvent implementations