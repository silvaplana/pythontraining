from math import sqrt


class Point:
    """Ma classe"""



    def __init__(self, aX=0, aY=0):
        self.x = aX
        self.y = aY

    def __repr__(self):
        s = f'x={self.x} y={self.y}'
        return s

    def __str__(self):
        s = f'abscisse={self.x} ordonne={self.y}'
        return s

    def move(self, dx, dy):
        self.x+=dx
        self.y+=dy

    def dist(self, aP):
        res = sqrt((aP.x - self.x) * (aP.x - self.x) + (aP.y - self.y) * (aP.y - self.y))
        return res



if __name__ == "__main__":
    print("================ debut ==================")
    p1 = Point(0, 0)
    print("p1  (str)=", p1)
    p2 = Point(1, 1)
    print("p2=", p2)
    print("distance p1 p2", p1.dist(p2))
    p3 = Point()
    print("p3=", p3)

    # deplace
    p1.move(1, 1)
    print("p1=", p1)
    p2.move(1, 1)
    print("p2=", p2)
    print("distance p1 p2 apres deplacment", p1.dist(p2))

