from tkinter import Tk

from tkintertutos.sicsinstaller.client.controller.Controller import Controller
from tkintertutos.sicsinstaller.server.model.Configuration import Configuration
from tkintertutos.sicsinstaller.server.model.Model import Model
from tkintertutos.sicsinstaller.server.resource.ModelResource import ModelResource
from tkintertutos.sicsinstaller.client.view.View import View


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
        view = View(fenetre, controller, aModelResource)
        model.registerModelEvent(view)


        fenetre.mainloop()

if __name__ == '__main__':
    app = App()