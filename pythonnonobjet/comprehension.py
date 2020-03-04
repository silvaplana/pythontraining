
################################################
# exo : comprehension
################################################
print("============== exo : comprehension ================")

liste =[1,2,3,4]
print ("liste de depart",liste)

# creer une liste de chiffre au carre:
print("\ncreer une liste de chiffre au carre:")
listC = [ el**2    for el in liste   ]
print(listC)

# creer une liste de nombre impair:
print("\ncreer une liste de nombre impair:")
listI = [ el for el in liste  if el%2==1   ]
print(listI)

# creer une liste de chiffre au cube contenant les nombres pairs:
print("\ncreer une liste de chiffre au cube contenant les nombres pairs:")
listCI = [  el**3 for el in liste  if el%2==0   ]
print(listCI)

