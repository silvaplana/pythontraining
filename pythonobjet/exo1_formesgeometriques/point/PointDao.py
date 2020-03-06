import sqlite3 as sql
from sqlite3 import OperationalError

from pythonobjet.exo1_formesgeometriques.point.Point import Point


class PointDao:
    """Ma classe"""

    def __init__(self):
        pass

    def initialisation(self):
        connecteur = sql.connect("donnee.db")
        curseur = connecteur.cursor()
        requete = "create table pointTable(col1 integer, col2 integer)"
        try:
            curseur.execute(requete)
        except OperationalError as e:
            print ("ope=",e)

        connecteur.commit()
        connecteur.close()


    def insertPoint (self, point):
        connecteur = sql.connect("donnee.db")
        curseur = connecteur.cursor()
        requete = f"insert into pointTable(col1, col2) values ({point.getX()},{point.getY()})"
        curseur.execute(requete)
        connecteur.commit()
        connecteur.close()


    def listePoints (self):
        listePoints = []

        connecteur = sql.connect("donnee.db")
        curseur = connecteur.cursor()

        requete = "select * from pointTable"
        curseur.execute(requete)

        for ligne in curseur.fetchall():
            listePoints.append(Point(ligne[0], ligne[1]))
        connecteur.close()
        return listePoints


if __name__ == "__main__":
    print("================ debut point dao ==================")

    #initialisation
    pointDao = PointDao()
    pointDao.initialisation()

    # insertion points
    p1 = Point(0,0)
    p2 = Point(1,1)
    pointDao.insertPoint(p1)
    pointDao.insertPoint(p2)

    #lister point
    listep = pointDao.listePoints()
    print("La liste est ", listep )




