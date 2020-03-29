import os
import shutil
from zipfile import ZipFile

import os.path
from os import path


class FileOp:
    def __init__(self):
        pass

    def removeFileOrDir (self, aPath):
        if aPath!=None and os.path.exists(aPath):
            if os.path.isfile(aPath):
                print("Removing file ", aPath)
                os.remove(aPath)
            elif os.path.isdir(aPath):
                print("Removing dir ", aPath)
                shutil.rmtree(aPath)

    def copyFileOrDir(self, srcPath, destDirPath):
        if srcPath!=None and os.path.exists(srcPath) and destDirPath!=None and os.path.exists(destDirPath):
            #s = srcPath.replace("/", "\\")
            #d = destDirPath.replace("/", "\\")
            print ("Copying", srcPath, "to", destDirPath)
            shutil.copy2(srcPath,destDirPath)

    def unzipFile(self, srcFilePath, destDirPath):
        with ZipFile(srcFilePath, "r") as zipObj:
            zipObj.extractall(destDirPath)

    def doesPathExist (self, aPath):
        return path.exists(aPath)



    # in a ascii file composed with line  composed with pattern  beacon1 = value  beacon2 = value , replaces the value for a specified beacon
    def replaceBeaconValueInFile(self, filePath, beacon, replacingValue):
        if not os.path.exists(filePath):
            print("The file", filePath, "does not exist")
            return

        f = open(filePath, "r")
        fileInArray = []
        for l in f:
            fileInArray.append(self.__replaceBeaconValue__(l, beacon, replacingValue))
        f.close()
        os.remove(filePath)

        f = open(filePath, "a")
        first = True
        for line in fileInArray:
            if first:
                f.write(line)
                first = False
            else:
                f.write(f"\n{line}")
        f.close()



    # in a string composed with pattern  beacon1 = value  beacon2 = value , replaces the value for a specified beacon
    def __replaceBeaconValue__(self, string, beacon, replacingValue):
        string2 = self.__removeBlanksBetweenBeaconAndEqual__(string, beacon)
        res = ""
        first = True
        for group in string2.split():
            newGroup = ""
            if not beacon in group:
                newGroup = group
            else:
                newGroup = f"{beacon}={replacingValue}"
            if first:
                res = newGroup
            else:
                res = res + " " + newGroup
            first = False
        return res

    # in a string composed with pattern  beacon1 = value  beacon2 = value ,   removes the blanks between beacon and value
    def __removeBlanksBetweenBeaconAndEqual__(self, string, beacon):
        if not beacon in string:
            return string
        finished = False
        f = string
        while not finished:
            f = f.replace(" =", "=")
            f = f.replace("= ", "=")
            if not (" =" in f or "= " in f):
                finished = True
        return f