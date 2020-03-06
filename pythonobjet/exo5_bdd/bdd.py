# sql -> requete sur un bd

#python

import sqlite3 as sql

connecteur = sql.connect( "donnee.db")
curseur = connecteur.cursor()


# creation table
#requete = "create table nomTable(col1 integer, col2 integer)"



# ecriture
for i in range(0,10):
    requete = f"insert into nomTable(col1, col2) values ({i},{i+1})"
    curseur.execute(requete)
    connecteur.commit()

# recupere
requete = "select * from nomTable where col1=1"
curseur.execute(requete)

# une seule valeur, la premiere de la table
#a = curseur.fetchone()   #recup sous forme de tuple
#print("res=", a)

for ligne in curseur.fetchall():
    print("ligne=", ligne)





connecteur.close()