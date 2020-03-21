import pickle

class Persistence:

    def __init__(self, model):
        self.model = model

    def saveAll(self):
        dico = {}
        with open(self.model.conf.backUpFile, "wb") as fic2:
            pickler = pickle.Pickler(fic2)
            pickler.dump(self.model.vals)
            print("persistence file saved vals is ", self.model.vals)

    def loadAll(self):
        res = {}
        # copy configuration
        for key in self.model.conf.vals:
            res[key] = self.model.conf.vals[key]

        # read file
        try:
            with open(self.model.conf.backUpFile, "rb") as file:
                unpickler = pickle.Unpickler(file)
                unpicklerDico = unpickler.load()

                # overwrite with loaded data
                for key in unpicklerDico:
                    res[key] = unpicklerDico[key]

        except FileNotFoundError as e:
            print("pas de fichier de pesistence")

        print ("loaded persistence is ",res)
        return res







