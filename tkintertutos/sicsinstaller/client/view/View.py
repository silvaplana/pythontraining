from tkinter import Label, StringVar, Button
from tkinter.ttk import Entry

from tkintertutos.sicsinstaller.client.view.ChangeDirButton import ChangeDirButton
from tkintertutos.sicsinstaller.client.view.ChannelsConfMenuButton import ChannelsConfMenuButton
from tkintertutos.sicsinstaller.client.view.PortComMenuButton import PortComMenuButton
from tkintertutos.sicsinstaller.client.view.RcuButton import RcuButton
from tkintertutos.sicsinstaller.server.event.ModelEvent import ModelEvent
from tkintertutos.toolbar.view.InfoLabel import InfoLabel


class View(ModelEvent):
    def __init__(self, window, controller, modelResource):
        self.window = window
        self.controller = controller
        self.model = modelResource
        ModelEvent.__init__(self)
        self.initMMI()


    def initMMI(self):

        currentLine = 0

        #Ligne 1 : info label
        currentLine+=1
        InfoLabel(self.window, "", self.controller).grid(row=currentLine, column=2)

        # Ligne 1 prime : vide
        currentLine += 1
        Label(self.window, text="Source and destination directories:", borderwidth=5, font='Helvetica 12 bold').grid(
            row=currentLine, column=2)

        # Ligne 2 : source
        currentLine += 1
        Label(self.window, text='Source directory:', borderwidth=5).grid(row=currentLine, column=1)
        self.sourceDest = StringVar()
        self.sourceDest.set(self.model.getSourceDest())
        Label(self.window, textvariable=self.sourceDest, borderwidth=5).grid(row=currentLine, column=2)
        ChangeDirButton(self.window, self.controller, "Change", "#sourceDest").grid(row=currentLine, column=3)

        # Ligne 3 : macs Hierarchy
        currentLine += 1
        Label(self.window, text='Macs hierarchy:', borderwidth=5).grid(row=currentLine, column=1)
        self.macsHierarchy = StringVar()
        self.macsHierarchy.set(self.model.getMacsHierarchy())
        Label(self.window, textvariable=self.macsHierarchy, borderwidth=5).grid(row=currentLine, column=2)
        ChangeDirButton(self.window, self.controller, "Change", "#macsHierarchy").grid(row=currentLine, column=3)

        # Ligne 4 : sics
        currentLine += 1
        Label(self.window, text='Sics hierarchy:', borderwidth=5).grid(row=currentLine, column=1)
        self.sicsHierarchy = StringVar()
        self.sicsHierarchy.set(self.model.getSicsHierarchy())
        Label(self.window, textvariable=self.sicsHierarchy, borderwidth=5).grid(row=currentLine, column=2)
        ChangeDirButton(self.window, self.controller, "Change", "#sicsHierarchy").grid(row=currentLine, column=3)

        # Ligne 5 : vide
        currentLine += 1
        Label(self.window, text="Remove:", borderwidth=5, font='Helvetica 12 bold').grid(
            row=currentLine, column=2)

        # Ligne 6 : remove macs data
        currentLine += 1
        RcuButton(self.window, self.controller, "Remove macs directory", "REMOVE", "macsDir").grid(row=currentLine, column=1)
        RcuButton(self.window, self.controller, "Remove macs data directory", "REMOVE", "macsDataDir").grid(row=currentLine, column=2)

        # Ligne 7 : remove sics data
        currentLine += 1
        RcuButton(self.window, self.controller, "Remove sics  directory", "REMOVE", "sicsDir").grid(row=currentLine, column=1)
        RcuButton(self.window, self.controller, "Remove sics data directory", "REMOVE", "sicsDataDir").grid(row=currentLine, column=2)

        # Ligne 7 prime : vide
        currentLine += 1
        Label(self.window, text="Copy , unzip:", borderwidth=5, font='Helvetica 12 bold').grid(
            row=currentLine, column=2)

        # Ligne i : elements a dezipper
        sourceZipElts = self.model.getZipElements(False)
        for el in range(len(sourceZipElts)):
            currentLine += 1
            RcuButton(self.window, self.controller, f"Remove remote {sourceZipElts[el]}", "REMOVE", sourceZipElts[el]).grid(row=currentLine, column=1)
            RcuButton(self.window, self.controller, f"Copy {sourceZipElts[el]}", "COPY", sourceZipElts[el]).grid(row=currentLine, column=2)
            RcuButton(self.window, self.controller, f"Unzip remote", "UNZIP", sourceZipElts[el]).grid(row=currentLine, column=3)

        # Ligne j : elements a copier
        sourceElts = self.model.getSourceElements(False)
        for el in range(len(sourceElts)):
            currentLine += 1
            RcuButton(self.window, self.controller, f"Remove remote {sourceElts[el]}", "REMOVE", sourceElts[el]).grid(row=currentLine, column=1)
            RcuButton(self.window, self.controller, f"Copy {sourceElts[el]}", "COPY", sourceElts[el]).grid(row=currentLine, column=2)

        # Ligne k : vide
        currentLine += 1
        Label(self.window, text="Change values:", borderwidth=5, font='Helvetica 12 bold').grid(
            row=currentLine, column=2)

        # Ligne l : definition label
        currentLine += 1
        Label(self.window, text='Label:', borderwidth=5).grid(row=currentLine, column=1)
        self.macsLabel = StringVar()
        self.macsLabel.set(self.model.getMacsLabel())
        Entry(self.window, textvariable=self.macsLabel, width=4).grid(row=currentLine, column=2)
        Button(self.window, text="Change", command=self.onChangeMacsLabelClick).grid(row=currentLine, column=3)

        # Ligne m : definition PORT COM
        currentLine += 1
        Label(self.window, text='Com port:', borderwidth=5).grid(row=currentLine, column=1)
        PortComMenuButton(self.window, self.controller, self.model.getMacsComPort()).grid(row=currentLine, column=2)
        Button(self.window, text="Change", command=self.onComPortChangeClick).grid(row=currentLine, column=3)

        # Ligne n : Configuration change
        currentLine += 1
        Label(self.window, text='Channels configuration:', borderwidth=5).grid(row=currentLine, column=1)
        self.channelsConf = StringVar()
        self.channelsConf.set(self.model.getMacsChannelsConf())
        ChannelsConfMenuButton(self.window, self.controller, self.model.getMacsChannelsConf()).grid(row=currentLine, column=2)
        Button(self.window, text="Change", command=self.onChannelsConfChangeClick).grid(row=currentLine, column=3)

        # Ligne o : vide
        currentLine += 1
        Label(self.window, text="", borderwidth=5, font='Helvetica 12 bold').grid(
            row=currentLine, column=2)


   # On click actions

    def onChangeMacsLabelClick(self):
        pass

    def onComPortChangeClick(self):
        pass

    def onChannelsConfChangeClick(self):
        pass

    #End on click actions




    # ModelEvent implementations


    def onMacsHierarchyUpdated(self, value):
        self.macsHierarchy.set(value)

    def onSicsHierarchyUpdated(self, value):
        self.sicsHierarchy.set(value)

    def onSourceDestUpdated(self, value):
        self.sourceDest.set(value)



    def onInfoLabelUpdate(self, value):
        pass



    # end of ModelEvent implementations