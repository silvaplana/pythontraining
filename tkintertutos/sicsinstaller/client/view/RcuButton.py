

# Button to remove, copy or unzip an element
from tkinter import Button


class RcuButton(Button):

    # operation : "REMOVE", "COPY" or "UNZIP"
    # hintSearch : "macs" , "sics", or "all"
    # element : a directory or a file name , can be preceeded by path.  There are special words : #macs , #sics , the root for macs and sics directories : below is data, below is...
    def __init__(self, window, controller, text,  operation, hintSearch, element ):
        Button.__init__(self, window)
        self.configure(text=text, command=self.onClick)
        self.controller = controller
        self.operation = operation
        self.hintSearch = hintSearch
        self.element = element
        self.refreshMMI()

    def onClick(self):
        if self.operation == "REMOVE":
            self.controller.removeFileOrDir(self.controller.getPath(self.element, self.hintSearch))
        if self.operation == "COPY":
            sourcePath = None
            destPath = None
            if not self.__isArchive__():
                for sourceEltWithPath in self.controller.getSourceElements(True):
                    if self.element in sourceEltWithPath:
                        sourcePath = sourceEltWithPath
                        break
                destPath = self.controller.getPath(self.element, self.hintSearch)
            else:
                for sourceEltZipWithPath in self.controller.getZipElements(True):
                    if self.element in sourceEltZipWithPath:
                        sourcePath = sourceEltZipWithPath
                        break
                if "macs" in self.element:
                    destPath = self.controller.getValue("macsHierarchy")
                elif "sics" in self.element:
                    destPath = self.controller.getValue("sicsHierarchy")

            if sourcePath == None:
                print ("Impossible to copy ",self.element," source path cannot be found")
            elif destPath == None:
                print("Impossible to copy ", self.element, " dest path cannot be found")
            self.controller.copyFileOrDir(sourcePath, destPath)
        if self.operation == "UNZIP":
            pathToUnzip = ""
            if self.hintSearch == "macs":
                pathToUnzip  = self.model.getValue("macsHierarchy")
            else:
                pathToUnzip = self.model.getValue("sicsHierarchy")
            zipElementPath = f"{pathToUnzip}/{self.element}"
            if self.controller.doesPathExist(zipElementPath):
                self.controller.unzipFile(self, zipElementPath, pathToUnzip)
            else:
                print("Cannot unzip element", self.element, ", path", zipElementPath,"does not exist" )


    def refreshMMI(self):
        if self.operation == "REMOVE" :
            # only enable remove if element exist in destination
            if not self.controller.getPath(self.element, self.hintSearch) == None:
                self.config(state='normal')
            else:
                self.config(state='disabled')

        if self.operation == "COPY" :
            # for archive elements, it is always possible to copy
            # for other elements, it is only possible to replace an existing element. if dest element doest not exist, don't enable copy
            if self.__isArchive__():
                self.config(state='normal')
            else:
              if self.controller.getPath(self.element, self.hintSearch) != None:
                  self.config(state='normal')
              else:
                  self.config(state='disabled')

        if self.operation == "UNZIP":
            # for zip element it is only possible to unzip if the zip is at the good place in dest hierarchy
            path = ""
            if self.hintSearch == "macs":
                path = self.controller.getValue("macsHierarchy")
            else:
                path = self.controller.getValue("sicsHierarchy")
            path += f"/{self.element}"
            if self.controller.doesPathExist(path):
                self.config(state='normal')
            else:
                self.config(state='disabled')

    def __isArchive__(self):
        if self.element.endswith("zip"):
            return True
        else:
            return False





