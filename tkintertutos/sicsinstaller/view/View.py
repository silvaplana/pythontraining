from tkinter import Label, StringVar, Button

from tkintertutos.sicsinstaller.model.ModelEvent import ModelEvent
from tkintertutos.sicsinstaller.view.ChangeDirButton import ChangeDirButton
from tkintertutos.sicsinstaller.view.RcuButton import RcuButton
from tkintertutos.toolbar.view.InfoLabel import InfoLabel


class View(ModelEvent):
    def __init__(self, window, controller, model):
        self.window = window
        self.controller = controller
        self.model = model
        ModelEvent.__init__(self)
        self.initMMI()


    def initMMI(self):
        self.bValue = StringVar()
        self.bValue.set(self.model.getBValue())
        button = Button(self.window, textvariable=self.bValue, command=self.onButtonClick)
        #button.pack()

        #Ligne 1
        InfoLabel(self.window, "", self.controller).grid(row=1, column=2)

        # Ligne 2 : source
        Label(self.window, text='Source directory:', borderwidth=5).grid(row=2, column=1)
        self.sourceDest = StringVar()
        self.sourceDest.set(self.model.getSourceDest())
        Label(self.window, textvariable=self.sourceDest, borderwidth=5).grid(row=2, column=2)
        ChangeDirButton(self.window, self.controller, "Change", self.sourceDest).grid(row=2, column=3)

        # Ligne 3 : macs
        Label(self.window, text='Macs directory:', borderwidth=5).grid(row=3, column=1)
        self.macsDest = StringVar()
        self.macsDest.set(self.model.getMacsDest())
        Label(self.window, textvariable=self.macsDest, borderwidth=5).grid(row=3, column=2)
        ChangeDirButton(self.window, self.controller, "Change", self.macsDest).grid(row=3, column=3)

        # Ligne 4 : sics
        Label(self.window, text='Sics directory:', borderwidth=5).grid(row=4, column=1)
        self.sicsDest = StringVar()
        self.sicsDest.set(self.model.getSicsDest())
        Label(self.window, textvariable=self.sicsDest, borderwidth=5).grid(row=4, column=2)
        ChangeDirButton(self.window, self.controller, "Change", self.sicsDest).grid(row=4, column=3)

        # Ligne 5 : vide
        Label(self.window, text="", borderwidth=5).grid(row=5, column=2)

        # Ligne 6 : remove macs data
        RcuButton(self.window, self.controller ,"Remove macs data directory", "REMOVE", "macsData").grid(row=6, column=1)
        RcuButton(self.window, self.controller ,"Remove macs directory", "REMOVE", "macsData").grid(row=6, column=3)

        # Ligne 7 : remove sics data
        Button(self.window, text="Remove sics data directory", command=self.onButtonClick).grid(row=7, column=1)
        Button(self.window, text="Remove sics  directory", command=self.onButtonClick).grid(row=7, column=3)

        sourceZipElts = self.model.getZipElements(False)
        for el in range(len(sourceZipElts)):
            Button(self.window, text=f"Remove remote {sourceZipElts[el]}", borderwidth=5).grid(row=8 + el, column=1)
            Button(self.window, text=f"Copy {sourceZipElts[el]}", borderwidth=5).grid(row=8 + el, column=2)
            Button(self.window, text=f"Unzip remote", borderwidth=5).grid(row=8 + el, column=3)

        print("toto", self.model.getSourceElements(False) )
        sourceElts = self.model.getSourceElements(False)
        for el in range(len(sourceElts)):
            Button(self.window, text=f"Remove remote {sourceElts[el]}", borderwidth=5).grid(row=8+ len(sourceZipElts)+el, column=1)
            Button(self.window, text=f"Copy {sourceElts[el]}", borderwidth=5).grid(row=8+ len(sourceZipElts)+el, column=2)

    # MMI actions

    def onButtonClick(self):
        self.controller.onClickOnButton()

    # MMI actions end

    # model event implementations
    def onButtonUpdated(self, value):
        self.bValue.set(value)
        print("onButtonUpdated value", value)

    def onInfoLabelUpdate(self, value):
        pass


    # end of model event implementations