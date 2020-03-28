from tkinter import Tk

from pythontraining.tkintertutos.sicsinstaller.client.controller.Controller import Controller
from pythontraining.tkintertutos.sicsinstaller.client.view.View import View
from pythontraining.tkintertutos.sicsinstaller.server.model.Configuration import Configuration
from pythontraining.tkintertutos.sicsinstaller.server.model.Model import Model
from pythontraining.tkintertutos.sicsinstaller.server.resource.ModelResource import ModelResource



class App:
    def __init__(self):

        ## Server ###########
        #model
        conf = Configuration()
        model = Model(conf)
        aModelResource = ModelResource(model)

        ## Client ###########
        #controller
        controller = Controller(aModelResource)
        # view
        fenetre = Tk()
        view = View(fenetre, controller)
        model.registerModelEvent(view)


        fenetre.mainloop()

if __name__ == '__main__':
    app = App()