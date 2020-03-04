
################################################
# exo : fonction
################################################

# ecrire une fonction qui calcule le volume
#arg: surperficie, hauteur par defaut

print ("==================exo 0 ==================================")

def computeVolume (superficie, hauteur=3.1 ):
    return superficie*hauteur

print ("volume pas par default=", computeVolume(1,1))
print ("volume par default=", computeVolume(1))

print ("==================exo 1  argument sans valeur par defaut : : on recup un tuple====")



## argument sans valeur par defaut : : on recup un tuple 
def addition(*toto):
    somme=0
    for r in toto:
        somme += r
    print(toto)
    return somme

print ("somme=",addition(1,2))
print ("somme=",addition(1,2,3,4))


print ("==================exo 2  valeurs par defaut (dico)==================================")

## argument avec valeur par defaut: on recup un dictionaire
# si j'ai prenom et nom, j'enregistre la fiche(renvoyer dico)
#si nom manque afficher nom manquant
#si prenom manque affaicher prenom manquant
def personnes(**kargs):
    if "nom" in kargs and "prenom" in kargs:
        return kargs
    else:
        if not "nom" in kargs:
            print ("nom manquant")
        if not "prenom" in kargs:
            print ("prenom manquant")

     

print(personnes (nom="RICHARD", prenom="Sebastien", civ="Mr"))
print(personnes (nom="RICHARD", civ="Mr"))
print(personnes (prenom="SEB", civ="Mr"))

print ("==================exo 3==================================")

## fonction: personne->
##  args nom , prenom, civilite
## retour: un dico
def personne( aNom, aPrenom, aCivilite ):
    return {"nom":aNom,"prenom":aPrenom, "civilite":aCivilite}

d = personne ("RICHARD", "SEB", "MR")
print(d)
