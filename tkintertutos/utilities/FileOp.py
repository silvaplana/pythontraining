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
            print ("Copying", srcPath, "to", destDirPath)
            shutil.copy2(srcPath,destDirPath)

    def unzipFile(self, srcFilePath, destDirPath):
        with ZipFile(srcFilePath, "r") as zipObj:
            zipObj.extractall(destDirPath)

    def doesPathExist (self, aPath):
        return path.exists(aPath)



    # in a ascii file composed with lines composed with pattern  key1 = value  key2 = value , replaces the value for a specified key
    def replaceValueInMutiKeyValueFile(self, filePath, key, replacingValue):
        if not os.path.exists(filePath):
            print("The file", filePath, "does not exist")
            return

        f = open(filePath, "r")
        fileInArray = []
        for l in f:
            fileInArray.append(self.__replaceValueInKeyValue__(l, key, replacingValue))
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



    # in a string composed with pattern  key1 = value  key2 = value , replaces the value for a specified key
    def __replaceValueInKeyValue__(self, string, key, replacingValue):
        string2 = self.__removeBlanksBetweenKeyAndEqual__(string, key)
        res = ""
        first = True
        for group in string2.split():
            newGroup = ""
            if not key in group:
                newGroup = group
            else:
                newGroup = f"{key}={replacingValue}"
            if first:
                res = newGroup
            else:
                res = res + " " + newGroup
            first = False
        return res

    # in a string composed with pattern  key1 = value  key2 = value ,   removes the blanks between key and value
    def __removeBlanksBetweenKeyAndEqual__(self, string, key):
        if not key in string:
            return string
        finished = False
        f = string
        while not finished:
            f = f.replace(" =", "=")
            f = f.replace("= ", "=")
            if not (" =" in f or "= " in f):
                finished = True
        return f