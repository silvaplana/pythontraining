

# Button to remove, copy or unzip an element
from tkinter import Button


class RcuButton(Button):

    # operation : "REMOVE", "COPY" or "UNZIP"
    # hintSearch : "macs" , "sics", or "all"
    # element : a directory or a file name , can be preceeded by path.  There are special words : #macs , #sics , the root for macs and sics directories : below is data, below is...
    def __init__(self, window, controller, text,  operation, hintSearch, element ):
        Button.__init__(self, window)
        self.configure(text=text)
        self.controller = controller
        self.operation = operation
        self.hintSearch = hintSearch
        self.element = element
        self.refreshMMI()

    def onClick(self):
        pass

    def refreshMMI(self):
        if self.operation == "REMOVE" or self.operation == "UNZIP" :
            if not self.controller.getPath(self.element, self.hintSearch) == None:
                print("button", self.element, self.hintSearch, " NORMAL")
                self.config(state='normal')
            else:
                print("button", self.element, self.hintSearch, "DISABLED")
                self.config(state='disabled')







