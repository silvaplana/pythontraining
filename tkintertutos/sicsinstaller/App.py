from tkinter import Tk, Label

from tkintertutos.sicsinstaller.model.Configuration import Configuration
from tkintertutos.sicsinstaller.model.Model import Model
from tkintertutos.sicsinstaller.view.View import View
from tkintertutos.toolbar.controller.Controller import Controller


class App:
    def __init__(self):

        #model
        conf = Configuration()
        model = Model(conf)

        #controller
        controller = Controller(model)

        # view
        fenetre = Tk()
        view = View(fenetre, controller, model)
        model.registerModelEvent(view)


        fenetre.mainloop()

if __name__ == '__main__':
    print("a")
    app = App()
    ("b")