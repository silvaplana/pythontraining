import random

from pendu.data import scores, gainPartieGagnee, gainPartiePerdue


def selectionneMotADecouvrir (aMots):
    return random.choice(aMots)


def afficher_mot (  aMotADecouvrir, aLettresTrouvees,  aLettre   ):
    res = ""
    for le in aMotADecouvrir:
        if le in aLettresTrouvees:
            res += le
        elif le==aLettre:
            res += le
            aLettresTrouvees.append(le)
        else:
            res += "*"
    return res

def updateScoreAfterPartie (aNomJoueur, aIsPartieGagnee ):

    score = 0
    if aNomJoueur in scores:
        score = scores[aNomJoueur]
    if aIsPartieGagnee:
        score+= gainPartieGagnee
    else:
        score += gainPartiePerdue
    scores[aNomJoueur] = score
    print ("Nouveau score du joueur " + aNomJoueur + " apres la partie=" , score )
    print ("Dico des scores =", scores)

    return None
