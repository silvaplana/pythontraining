
from pendu.data import mots, nbCoupsMax
from pendu.operations import selectionneMotADecouvrir, afficher_mot, updateScoreAfterPartie

lettresTrouvees = []
compteurCoups = 0


if __name__ == "__main__":
    print("================ debut ==================")

    nomJoueur = input ("QUel est votre nom")


    motADecouvrir = selectionneMotADecouvrir(mots)

    print("L'ordinateur a choisi le mot masqué a découvrir est:", motADecouvrir)

    motMasque = afficher_mot ( motADecouvrir, lettresTrouvees, "" )

    print("Le mot masque est:", motMasque)


    isPartieGagnee = False

    while compteurCoups< nbCoupsMax:
        compteurCoups +=1
        print ("======Essai numero", compteurCoups, ".", nbCoupsMax, " max========")

        lettre = input("Choissisez une lettre")

        motMasque = afficher_mot ( motADecouvrir, lettresTrouvees , lettre )
        print("resultat de l'essai:", motMasque)


        if motMasque != motADecouvrir:
            print("Mot pas encore trouvé totalement")
            if compteurCoups >= nbCoupsMax:
                print("La partie est terminee. Le mot n'est pas trouvé")
                break
        else:
            print("C'est gagné!!!!!  Bravo. partie terminee")
            isPartieGagnee = True
            break

    updateScoreAfterPartie(nomJoueur, isPartieGagnee)

