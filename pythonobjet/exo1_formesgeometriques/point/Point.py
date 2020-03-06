from math import sqrt


class Point:
    """Ma classe"""



    def __init__(self, aX=0, aY=0):
        self.__x = aX
        self.__y = aY

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    #def setX(self, x):
    #    self.__x = x
    #def setY(self, y):
    #    self.__y = y
    #x = property(getX, setX )

    @property
    def x(self):
        return "pas access"

    @x.setter
    def x(self, val):
        print('pas modifiable')


    def __repr__(self):
        s = f'Pointrepr(x={self.__x} y={self.__y})'
        return s

    def __str__(self):
        s = f'Pointstr(x={self.__x} y={self.__y})'
        return s

    #def __sub__(self, autre):
    #    print ("in sub begin p=", self)
    #    d = self.dist(autre)
    #    print("in sub end  p=", self)
    #    return d



    def dist(self, aP):
        return  sqrt((aP.getX()) - self.__x)**2 + (aP.getY() - self.__y)**2

    def move(self, dx, dy):
        self.__x+=dx
        self.__y+=dy


if __name__ == "__main__":
    print("================ debut ==================")
    p1 = Point(0, 0)
    print("p1  (str)=", p1)
    p2 = Point(1, 1)
    print("p2=", p2)
    print("distance p1 p2", p1.dist(p2))


    #d = p2 - p1
    #print("d=", d)


    # deplace
    p1.move(1, 1)
    print("p1=", p1)
    p2.move(1, 1)
    print("p2=", p2)
    print("distance p1 p2 apres deplacment", p1.dist(p2))

