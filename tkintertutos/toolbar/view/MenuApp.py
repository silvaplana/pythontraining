from tkinter import Menu
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo


class MenuApp():
    def __init__(self, root, controller):
        self.controller = controller
        self.menubar = Menu(root)
        menu1 = Menu(self.menubar, tearoff=0)
        menu1.add_command(label="Load", command=self.onClickLoadFile)
        menu1.add_command(label="UnLoad", command=self.onClickUnLoadFile)
        menu1.add_separator()
        menu1.add_command(label="Quit", command=root.quit)
        self.menubar.add_cascade(label="File", menu=menu1)

        menu2 = Menu(self.menubar, tearoff=0)
        menu2.add_command(label="Cut", command=self.alert)
        menu2.add_command(label="Copy", command=self.alert)
        menu2.add_command(label="Paste", command=self.alert)
        self.menubar.add_cascade(label="Edit", menu=menu2)

        menu3 = Menu(self.menubar, tearoff=0)
        menu3.add_command(label="About", command=self.alert)
        self.menubar.add_cascade(label="Help", menu=menu3)

        root.config(menu=self.menubar)

    def alert(self):
        showinfo("alerte", "Bravo!")

    def onClickLoadFile(self):
        filepath = askopenfilename(title="LoadFile", filetypes=[('all files', '.*')])
        print("on load file: ", filepath)
        self.controller.onClickLoadFile(filepath)

    def onClickUnLoadFile(self):
        pass