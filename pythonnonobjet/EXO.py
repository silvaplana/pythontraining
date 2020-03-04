from math import sqrt

# point dico  "x"  "y"
# fonction qui permet d'init un point
# fontion d'affichage du point :retourn une string
# fonction permettant de deplacer un point
# fonction de distance entre 2 points

def init (x, y):
    return { "x":x, "y":y }

def toString ( point):
    s = f'abscisse={point["x"]} ordonne={point["y"]}'
    return s

def move ( point , dx, dy):
    point["x"] = point["x"]+dx
    point["y"] = point["y"]+dy

def dist ( aP1 , aP2):
    res = sqrt ( (aP2["x"]-aP1["x"])*(aP2["x"]-aP1["x"])  + (aP2["y"]-aP1["y"])*(aP2["y"]-aP1["y"]))
    return res



#init
p1 = init (0,0)
print ("p1=",toString(p1))
p2 = init (1,1)
print ("p1=",toString(p2))
print ("distance p1 p2",dist(p1,p2))

#deplace
move(p1, 1,1)
print ("p1=",toString(p1))
move(p2,1,1)
print ("p2=",toString(p2))
print ("distance p1 p2 apres deplacment",dist(p1,p2))

