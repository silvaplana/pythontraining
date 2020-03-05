from math import pi

from pythonobjet.point.Point import Point


class FigureGeometrique:

    def __init__(self, origine):
        self.origine = origine

    def move(self, dx, dy):
        self.origine.move(dx, dy)

    def surface(self):
        pass

    def perimetre(self):
        pass

    def afficher(self):
        pass


class Rectangle(FigureGeometrique):
    """Ma classe"""

    def __init__(self, origine, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
        FigureGeometrique.__init__(self, origine)


    def toString(self):
        s = f'rectangle origine={self.origine} longueur={self.longueur} larger={self.largeur} perimeter={self.perimetre()} surface={self.surface()}'
        return s

    def perimetre(self):
        return 2 * (self.largeur + self.longueur)

    def surface(self):
        return self.largeur * self.longueur


class Cercle(FigureGeometrique):
    """Ma classe"""

    def __init__(self, origine, rayon):
        self.rayon = rayon
        FigureGeometrique.__init__(self, origine)

    def toString(self):
        s = f'cercle: origine={self.origine} rayon={self.rayon} perimeter={self.perimetre()} surface={self.surface()}'
        return s

    def perimetre(self):
        return 2 * pi * self.rayon

    def surface(self):
        return pi * self.rayon * self.rayon


if __name__ == "__main__":
    print("================ debut rectangle ==================")
    rect = Rectangle(Point(0, 0), 2, 2)
    print("rectangle=", rect.toString())

    # deplace
    rect.move(1, 1)
    print("rectangle apres deplacement=", rect.toString())

    print("================ debut cercle ==================")

    cerc = Cercle(Point(0, 0), 3)
    print("cercle=", cerc.toString())


