from random import randrange


################################################
# exo : jeu roulette
################################################
print("============== exo : jeu roulette ================")
##annee = int(input("Quelle année?"))

capitalJoueur = 5
nbreDeTours =0
fini = False

while nbreDeTours<20 and not fini:

    # mise et boule?   
    quelleBoule = int(input("Sur quelle boule entre 1 et 50 misez vous "))
    quelleMise = int(input("Quelle mise "))

    

    # lancer la roulette
    resultatJeu = randrange(50)
    print("resultatjeu=",resultatJeu)

    # analyse resultat
    couleurMaBoule = quelleBoule%2
    print("couleurMaBoule=",couleurMaBoule)
    couleurResultat = resultatJeu%2
    print("couleurResultat=",couleurResultat)
    gain=0
    if quelleBoule == resultatJeu:
        gain = 2*quelleMise
        capitalJoueur+=gain
        print("Bravo. Votre boule egale resultat. Gain =",gain,"Nouveau capital=",capitalJoueur)
    elif couleurMaBoule == couleurResultat:
        gain = quelleMise/2
        capitalJoueur+=gain
        print("Bravo. Meme couleur de boule. Gain =",gain,"Nouveau capital=",capitalJoueur)
    else:
        gain-=quelleMise
        capitalJoueur+=gain
        print("Perdu!! sniff .Gain =",gain,"Nouveau capital=",capitalJoueur)
        
    # fin du tour
    if capitalJoueur <= 0:
        print ("Plus de sous, on arrete!!!")
        fini = True
    else:
        stopOuEncore = input ("Stop pour arreter. Sinon Return")
        if "stop" in stopOuEncore.lower():
            print ("Ok, on arrete!!!")
            fini = True
   
    


    

