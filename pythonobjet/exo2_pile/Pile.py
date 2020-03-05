from pythonobjet.exo2_pile.PileException import PileExceptionPleine, PileExceptionVide, PileException


class Pile:
    """Ma classe"""

    def __init__(self, tailleMax):
        self.__tailleMax = tailleMax
        self.__data = []
        print("Vous avez cree une pile de taille max", tailleMax)


    @property
    def tailleMax(self):
        return self.__tailleMax

    @tailleMax.setter
    def tailleMax (self, val):
        print("non modifiable")


    def empiler (self, obj):
        if len(self.__data) < self.__tailleMax:
            self.__data.append(obj)
        else:
            raise PileExceptionPleine()
            print("taille max", self.__tailleMax, " atteinte")

    def depiler(self):
        if len(self.__data)!=0:
            return self.__data.pop()
        else:
            raise PileExceptionVide()
            print("Pas possible de depiler")


    def __str__(self):
        return f"La pile contient {len(self.__data)} elements. pile = {self.__data}"

    def __len__(self):
        return len(self.__data)


if __name__ == "__main__":

    # creation
    print("================ debut ==================")
    p = Pile(2)

    print("taillemax est ", p.tailleMax)
    p.tailleMax = 5

    # empiler

    try:
        p.empiler(10)
        p.empiler(20)
        p.empiler(30)
    except PileException as e:
        print ("There is an exception 1", e)


    # afficher
    print ("La pile est: ", p)

    # empiler
    try:
        print("res depilage 1:", p.depiler())
        print("res depilage 2:", p.depiler())
        print("res depilage 3:", p.depiler())
    except PileException as e:
        print ("There is an exception 1", e)