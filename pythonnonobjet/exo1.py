################################################
# exo : annee bisextile
################################################
print("============== exo : annee bisextile ================")
##annee = int(input("Quelle année?"))
annee = 2020
print(annee)

if ((annee%4 == 0) and (annee%100 != 0)) or (annee%400 == 0):
    print( str(annee) + " est bissextile")
else :
    print( str(annee) + " n est pas bissextile")


################################################
# exo : nombres divisibles par 9
################################################
print("============== exo : nombres divisibles par 9 ================")
compteur = 0
i=0
while compteur<20:
   i += 1
   if i%9 == 0:
       print ( str(i) + "est divisible par 9")
       compteur += 1

################################################
# exo : suite fibonacci
################################################
print("============== exo : suite fibonacci ================")
compteur = 0
avantDernier = 1
dernier = 1
while compteur<20:
   nouv = avantDernier + dernier
   print ( nouv ,"est nombre de fibonacci")
   # pour prochain
   avantDernier = dernier
   dernier = nouv
   compteur += 1


################################################
# exo : Afficher caque lettre de votre prénom puis uniquezment les voyelles
################################################
print("============== exo : Afficher caque lettre de votre prénom puis uniquezment les voyelles ================")
prenom = "SEBASTIEN"
print ("mon prenom=")
for char in prenom:
    print (char)

print ("mes voyelles=")
for char in prenom:
    if char.lower() in "aeiou":
        print (char)

