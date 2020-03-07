import threading
import time

class DelayedLoadingDirectory(threading.Thread):
    def __init__(self, filepath, controller, fileCategories):
        threading.Thread.__init__(self)
        self.filepath =filepath
        self.controller = controller
        self.fileCategories = fileCategories

    def run (self):
        print("delayed load")
        time.sleep(1)
        self.controller.onLoadDirectoryStepCompletedEvent(f"     Loading app (1/7)...", False, self.fileCategories)
        time.sleep(1)
        self.controller.onLoadDirectoryStepCompletedEvent(f"     Loading segmented (4/7)...", False, self.fileCategories)
        time.sleep(1)
        self.controller.onLoadDirectoryStepCompletedEvent(f"l", True, self.fileCategories)
        time.sleep(1)

class Model():

    def __init__(self):
        pass
        self.controller = None
        self.counter = 0

    def setController(self, controller):
        self.controller = controller

    def loadFile(self, filepath):
        print ("Load File:", filepath)
        res = ""
        f = open(filepath, "r")
        for l in f:
            res +=l
        f.close()
        self.controller.onLoadFileStepCompleted("", True)
        return res

    def getFileFromLoadDirectory(self, fileName):
        dico = { "app":"text app",
                 "serial":"text serial",
                 "relay":"text relay", "mopdLog":"text mopdlog","mopdStat":"text mopd stat" }


    def loadDirectory (self, filepath):
        print("Load Directory:", filepath)
        a = DelayedLoadingDirectory(filepath, self.controller, self.getFileCategories())
        a.start()


    def getFileCategories(self):
        return ["app", "serial", "relay", "mopdLog","mopdStat"]
