
################################################
# exo : dictionnaire
################################################
print("============== exo : dictionnaire ================")


# nom, prenom civilité

personne = { "nom":"Richard", "prenom":"Sébastien", "civilité":"Monsieur"}

print("=================================   ")
for key in personne:# si on itere sur un dict, on itere sur les clés
    print(key,"=", personne[key])


print("=================================:keys()")
for key in personne.keys():
    print(key,"=", personne[key])

print("================================= values()")
for value in personne.values():
    print(value)

print("=================================: items()")
for key, value in personne.items():   # key,value est un tuple
    print(key,"=", value)

