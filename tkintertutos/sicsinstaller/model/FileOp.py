import os
import re


class FileOp:
    """path operations"""


    def getDir(self, path, dirName):
        for root, dirs, files in os.walk(path):
            if root.endswith(f"\\{dirName}"):
                return root

    def getFileNameWithoutExtensionNorFigure(self, originalFilename):
        res = originalFilename.split(".")[0]
        res = re.sub('\d+', '', res)
        return res

    def listAllLogFilesInData(self, path, dirName, completeNames=True, withExtensionAndFigure=True):
        for root, dirs, files in os.walk(path):
            if root.endswith(f"\\{dirName}"):
                res = []
                for fil in files:
                    formattedName = ""
                    if completeNames:
                        formattedName = f"{root}\\{fil}"
                    else:
                        formattedName = fil
                    if not withExtensionAndFigure:
                        formattedName = self.getFileNameWithoutExtensionNorFigure(formattedName)
                    res.append(formattedName)
                return list(set(res))