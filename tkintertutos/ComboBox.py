from tkinter import tix


def Affiche(evt):
    print ("eeee", varcombo.get()) ## On affiche a l'ecran la valeur selectionnee

root = tix.Tk()
varcombo = tix.StringVar()
combo = tix.ComboBox(root, editable=1, dropdown=1, variable=varcombo, command = Affiche)
combo.entry.config(state='readonly')  ## met la zone de texte en lecture seule
combo.insert(0, 'NT')
combo.insert(1, 'Linux')
combo.insert(2, 'apple')
combo.insert(3, 'android')
combo.insert(4, 'next')
combo.pack()
root.mainloop()