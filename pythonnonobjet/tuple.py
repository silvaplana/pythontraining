
################################################
# exo : tuple
################################################
print("============== exo : tuple ================")


eleve = [ ("math", 15), ("histoire", 6), ("francais", 12), ("anglais", 10),("sport", 16)]


print("liste des eleves de depart", eleve)
# enoncé trier cette liste selon les notes

# 1: inverser les tuples:
eleve = [ (note,matiere) for matiere, note in eleve ]
print ("tuples inversés=", eleve)

# 2: trier selon note
eleve.sort()
print ("trier selon note=", eleve)

#3: reinverser
eleve = [ (matiere, note) for matiere, note in eleve ]
print ("Resultat final=", eleve)


    

