class Pile:
    """Ma classe"""



    def __init__(self, tailleMax):
        self.__tailleMax = tailleMax
        self.__data = []
        print("Vous avez cree une pile de taille max", tailleMax)

    def empiler (self, obj):
        if len(self.__data) < self.__tailleMax:
            self.__data.append(obj)
        else:
            print("taille max", self.__tailleMax, " atteinte")

    def depiler(self):
        if self.__data.__len__()!=0:
            return self.__data.pop()
        else:
            print("Pas possible de depiler")


    def __str__(self):
        return f"La pile contient {len(self.__data)} elements. pile = {self.__data}"

    def __len__(self):
        return len(self.__data)

    def getSize(self):
        return len(self.__data)


if __name__ == "__main__":

    # creation
    print("================ debut ==================")
    p = Pile(3)

    # empiler
    p.empiler(10)
    p.empiler(20)
    p.empiler(30)

    # afficher
    print ("La pile est: ", p)

    # empiler
    print("res depilage 1:", p.depiler())
    print("res depilage 2:", p.depiler())
    print("res depilage 3:", p.depiler())
    print("res depilage 3:", p.depiler())