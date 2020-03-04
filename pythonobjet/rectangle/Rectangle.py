from pythonobjet.point.Point import Point


class Rectangle:
    """Ma classe"""

    def __init__(self, origine, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
        self.origine = origine

    def toString(self):
        s = f'origine={self.origine.toString()} longueur={self.longueur} larger={self.largeur} perimeter={self.perimetre()} surface={self.surface()}'
        return s

    def move(self, dx, dy):
        self.origine.move(dx, dy)

    def perimetre(self):
        return 2 * (self.largeur + self.longueur)

    def surface(self):
        return self.largeur * self.longueur


if __name__ == "__main__":
    print("================ debut ==================")
    rect = Rectangle(Point(0, 0), 2, 2)
    print("rectangle=", rect.toString())

    # deplace
    rect.move(1, 1)
    print("rectangle apres deplacement=", rect.toString())
