from tkinter import*



fenetre = Tk()


w = Label(fenetre, text="eeeee")

value = StringVar()
value.set("texte par défaut")
entree = Entry(fenetre, textvariable="eeeee", width=30)
entree.pack()
w.pack()




fenetre.mainloop()



