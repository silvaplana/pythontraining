import os
import threading
from time import sleep

from pythontraining.tkintertutos.sicsinstaller.server.model.Persistence import Persistence
from pythontraining.tkintertutos.utilities.FileOp import FileOp


class ReplaceFileThread(threading.Thread):
    def __init__(self, model, element, duration):
        threading.Thread.__init__(self)
        self.model = model
        self.element = element
        self.duration = duration
        self.msg = f"Copying {self.element}"

    def run(self):
        while self.duration >= 0:
            self.model.modelEvent.onInfoLabelUpdate(self.msg)
            sleep(1)


class Model:
    def __init__(self, conf):
        self.fileOp = FileOp()
        self.conf = conf
        self.persistence = Persistence(self)
        # vals are stored in persistence
        # keys are : macsHierarchy, sicsHierarchy, sourceDir, macsLabel, macsComPort, MacsChannelsConf
        self.vals = {}
        self.__loadConf()

    def registerModelEvent(self, modelEvent):
        self.modelEvent = modelEvent

    def getValue(self, key):
            if key in self.vals.keys():
                return self.vals[key]
            else:
                return f"not found {key}"

    def setValue(self, key, value):
            if key in self.vals.keys():
                self.vals[key] = value
                self.persistence.saveAll()
                self.modelEvent.onValueUpdated(key, value)
            else:
                return  print ("not found", key, ": impossible to set value")


    def getZipElements(self, withPath):
        zipElements = []
        sourceDir = self.vals["sourceDir"]
        if sourceDir == None:
            return []
        else:
            for file in os.listdir(sourceDir):
                if file.endswith(".zip"):
                    zipElements.append(file)

            if not withPath:
                return zipElements
            else:
                zipElements2 = []
                for e in zipElements:
                    zipElements2.append(f"{self.getSourceDest()}\\{e}")
                return zipElements2

    def getSourceElements(self, withPath):
        sourceElements = []
        sourceDir = self.vals["sourceDir"]
        if sourceDir == None:
            return []
        else:
            for root, dirs, files in os.walk(sourceDir):
                for name in files:
                    if not name.endswith(".zip") and self.getPath(name)!=None:
                        if not withPath:
                            sourceElements.append(name)
                        else:
                            sourceElements.append(os.path.join(root, name))
                            sourceElements[-1] = sourceElements[-1].replace("\\", "/")
            return sourceElements

    def onMacsLabelApply(self):
        path = self.getPath( "fr.dga.sics.profile.cfg", "sics")
        if path == None:
            print("Cannot apply onMacsLabelApply, path fr.dga.sics.profile.cfg cannot be found")
            return
        self.fileOp.replaceBeaconValueInFile(path, "participantId", self.getValue("macsLabel"))

    def onMacsComPortApply(self):
        path = self.getPath("com.bull.mil.macs.conf.xml", "macs")
        if path == None:
            print("Cannot apply onMacsLabelApply, path com.bull.mil.macs.conf.xml cannot be found")
            return
        selectedMacsPort = self.getValue("macsComPort")
        if selectedMacsPort == 'PIMS':
            newMacsPort =  "\"tcp://localhost/COM240\""
        else:
            newMacsPort = f"\"serial://{selectedMacsPort}\""
        self.fileOp.replaceBeaconValueInFile(path, "uri", newMacsPort)

    def onMacsChannelsConfApply(self):
        path = self.getPath("com.bull.mil.macs.conf.xml", "macs")
        if path == None:
            print("Cannot apply onMacsLabelApply, path com.bull.mil.macs.conf.xml cannot be found")
            return
        values = self.getValue("macsChannelsConf").split(",")
        publicChannel=f"\"{values[0]}\""
        privateChannel = f"\"{values[1]}\""
        self.fileOp.replaceBeaconValueInFile(path, "public-channel", publicChannel)
        self.fileOp.replaceBeaconValueInFile(path, "private-channel", privateChannel)

    # get path in macs hierarchy (option="macs")  or sics hierarchy  (option="sics") or both hierarchy (option="all")
    # hintSearch : "macs" , "sics", or "all"
    # element : a directory or a file name , can be preceeded by path.  There are special words : #macs , #sics , the root for macs and sics directories : below is data, below is...
    def getPath(self, element, hintSearch="all"):

        strElement = element

        # replace #macs  and #sics by their path
        if "#macs" in strElement:
            if not self.__getMacsDir() == None:
                strElement = strElement.replace("#macs", self.__getMacsDir())
            else:
                return None

        if "#sics" in strElement:
            if not self.__getSicsDir() == None:
                strElement = strElement.replace("#sics", self.__getSicsDir())
            else:
                return None

        strTmp = ""
        pathFound = None

        if (hintSearch == "macs" or hintSearch == "all") and "macsHierarchy" in  self.vals:
            pathFound = self.__getPathThatEndsWith(self.vals["macsHierarchy"], strElement)
            if pathFound != None:
                return pathFound

        if (hintSearch == "sics" or hintSearch == "all") and "sicsHierarchy" in  self.vals:
            pathFound = self.__getPathThatEndsWith(self.vals["sicsHierarchy"], strElement)
            if pathFound != None:
                return pathFound
        return None

    def removeFileOrDir(self, path):
        if path != None and os.path.exists(path):
            self.modelEvent.onInfoLabelUpdate(f"Deleting element {path}...")
            self.fileOp.removeFileOrDir(path)
            self.modelEvent.onFileOrDirUpdated(f"{path} deleted", "deleted" )
        else:
            self.modelEvent.onInfoLabelUpdate(f"{path} cannot be copied ")



    def copyFileOrDir(self, srcPath, destDirPath):
        if srcPath!=None and os.path.exists(srcPath) and destDirPath!=None and os.path.exists(destDirPath):
            self.modelEvent.onInfoLabelUpdate(f"Copying element {srcPath} to {destDirPath} ...")
            self.fileOp.copyFileOrDir(srcPath, destDirPath)
            self.modelEvent.onFileOrDirUpdated(f"{srcPath} copied","copied")
        else:
            self.modelEvent.onInfoLabelUpdate(f"{srcPath} cannot be copied ")

    def unzipFile(self, srcFilePath, destDirPath):
        if srcFilePath != None and os.path.exists(srcFilePath) and destDirPath != None and os.path.exists(destDirPath):
            self.modelEvent.onInfoLabelUpdate(f"Unzipping element {srcFilePath} to {destDirPath} ...")
            self.fileOp.unzipFile(srcFilePath, destDirPath)
            self.modelEvent.onFileOrDirUpdated(f"{srcFilePath} unzipped","unzipped")
        else:
            self.modelEvent.onInfoLabelUpdate(f"{srcFilePath} cannot be unzipped")

    def doesPathExist(self, path ):
        return self.fileOp.doesPathExist( path)

    ## private methods

    def __loadConf(self):
        self.vals = self.persistence.loadAll()

    #def __replaceFile(self, element):
    #    ReplaceFileThread(self, element, 4).start()

    def __getMacsDir(self):
        pattern = "/bin/macs-sics-server-runtime.cmd"

        pathFound = self.__getPathThatEndsWith (self.vals["macsHierarchy"], pattern)
        if pathFound == None:
            return None
        pathFound = pathFound.replace(pattern, "")
        return pathFound

    def __getSicsDir(self):
        pattern = "/factory/fr.dga.sics.profile.cfg"
        pathFound = self.__getPathThatEndsWith(self.vals["sicsHierarchy"], pattern)
        if pathFound == None:
            return None
        pathFound = pathFound.replace(pattern, "")
        return pathFound

    def __getPathThatEndsWith (self, startPath, endsWithStr):
        for root, dirs, files in os.walk(startPath):
            for name in files:
                strTmp = os.path.join(root, name)
                strTmp = strTmp.replace("\\", "/")
                if strTmp.endswith(endsWithStr):
                    return strTmp
            for name in dirs:
                strTmp = os.path.join(root, name)
                strTmp =  strTmp.replace("\\", "/")
                if strTmp.endswith(endsWithStr):
                    return strTmp
        return None