
################################################
# exo : liste
################################################
print("============== exo : liste ================")

jourSemaine=["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]

#afficher le mercredi:
print("\nafficher le mercredi:")
print(jourSemaine[2])

#afficher le samedi par la fin:
print("\nafficher le samedi par la fin:")
print(jourSemaine[-2])

# supprimer le jeudi:
print("\nsupprimer le jeudi:")
jourDeSemaine2=[]
jourDeSemaine2 = jourSemaine[:3]+jourSemaine[4:]
jourSemaine = jourDeSemaine2
print(jourSemaine)


#Remplacer vendredi par jeudi:
print("\nRemplacer vendredi par jeudi:")
jourSemaine[3]="jeudi"
print(jourSemaine)


#Ajouter le vendredi entre le jeudi et le samedi:
print("\nAjouter le vendredi entre le jeudi et le samedi:")
jourDeSemaine2=[]
jourDeSemaine2 = jourSemaine[:4]+ ["vendredi"]+ jourSemaine[4:]
jourSemaine=jourDeSemaine2
print(jourSemaine)

#afficher chaque jour de cette facon:
print("\nafficher chaque jour de cette facon:")
for jour in jourSemaine:
    print (jour)
    if jour == "vendredi":
        print ("c est le we")
    

