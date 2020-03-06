#WRITE :
# r = read
# w = ecrture avec ecrasement
# a = ecriture a la suite
# b = binaire -> rb  / wb   / ab
f = open("fichier2.txt", "a" )
f.write("\nlligne1zz")
f.write("\nligne2ee")
# IMPORTANT
f.close()


#READ
f = open ("fichier2.txt", "r")
for l in f:
    print(l, end="")
f.close()


#ContextManager
print("******************* context manager *****************")
with open("fichier2.txt", "r") as fic:
    for l in fic:
        print(l, end="")
    print("\nfin dans closed=", fic.closed)

print("\nfin hors with=", fic.closed)

#pickle
import pickle

dico= {'elt1':1,  'elt2':2, 'elt3':3  }

#with open("fichierPickle.bin", "wb") as fic2:
#    pickler = pickle.Pickler(fic2)
#    pickler.dump(dico)

with open("fichierPickle.bin", "rb") as fic2:
    unpickler = pickle.Unpickler(fic2)
    dico2 = unpickler.load()

print ("dico2", dico2)