from tkinter import Tk, Label

from tkintertutos.sicsinstaller.model.Configuration import Configuration
from tkintertutos.sicsinstaller.model.Model import Model
from tkintertutos.sicsinstaller.model.modelResource.ModelResource import ModelResource
from tkintertutos.sicsinstaller.view.View import View
from tkintertutos.toolbar.controller.Controller import Controller


class App:
    def __init__(self):

        #model
        conf = Configuration()
        model = Model(conf)
        modelResource = ModelResource(model)

        #controller
        controller = Controller(modelResource)
        # view
        fenetre = Tk()
        view = View(fenetre, controller, modelResource)
        model.registerModelEvent(view)


        fenetre.mainloop()

if __name__ == '__main__':
    print("a")
    app = App()
    ("b")