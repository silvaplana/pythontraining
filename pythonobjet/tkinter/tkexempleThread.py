import threading
from time import sleep
from tkinter import*

class MonBoutonQuiMarcheThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run (self):
        print("quit 2")

        valueQuiMarche.set("gros calcul qui marche 1/3...")
        sleep(2)
        valueQuiMarche.set("gros calcul qui marche 2/3...")
        sleep(2)
        valueQuiMarche.set("gros calcul qui marche3/3...")
        sleep(2)
        valueQuiMarche.set("Fin gros calcul qui marche ...")


def boutonQuiMarchePas():
    valueQuiMarchePas.set("gros calcul 1/3...")
    sleep(2)
    valueQuiMarchePas.set("gros calcul 2/3...")
    sleep(2)
    valueQuiMarchePas.set("gros calcul 3/3...")
    sleep(2)
    valueQuiMarchePas.set("Fin gros calcul...")


def boutonQuiMarche():
    t = MonBoutonQuiMarcheThread()
    t.start()

if __name__ == '__main__':
    fenetre = Tk()
    #bouton qui marche pas
    valueQuiMarchePas = StringVar()
    valueQuiMarchePas.set("bouton qui marche pas")
    boutonQuiMarchePas=Button(fenetre, textvariable=valueQuiMarchePas, command=boutonQuiMarchePas)
    boutonQuiMarchePas.pack()

    #bouton qui marche
    valueQuiMarche = StringVar()
    valueQuiMarche.set("bouton qui marche")
    boutonQuiMarche=Button(fenetre, textvariable=valueQuiMarche, command=boutonQuiMarche)
    boutonQuiMarche.pack()
    fenetre.mainloop()



