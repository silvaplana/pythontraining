from tkinter import *

class TestMenu:
        def __init__(self, master):
            self.master = master

            self.top = Toplevel(width=200, relief=RAISED, borderwidth=2)
            self.menubar = Menubutton(self.top, text='Menubutton', relief=RAISED,
                                      activebackground='#3399ff', bg='white', fg='black')
            self.menubar.pack(side="top")

            mb_radmenu = Menu(self.menubar)
            self.menubar.configure(menu=mb_radmenu)

            mb_radmenu.add_radiobutton(label='A')
            mb_radmenu.add_radiobutton(label='B')
            mb_radmenu.add_radiobutton(label='C')

def main():
    root = Tk()
    root.withdraw()
    app = TestMenu(root)
    root.mainloop()

if __name__ == '__main__':
    main()