import sys
import os
sys.path.append(os.path.join(__file__,"../"))
from rpg import *
from guerrier import Guerrier
from mage import Mage
opposant=Mage("j2",10)
p1=Guerrier("j1",3)
p1.combat(opposant)

joueur1 = Joueur("Joueur1", 3)

personnage1 = Personnage("Pseudo1")
personnage2 = Personnage("Pseudo2")
personnage3 = Personnage("Pseudo3")

joueur1.ajouter_personnage(personnage1)
joueur1.ajouter_personnage(personnage2)
joueur1.ajouter_personnage(personnage3)

joueur1.eliminer_numero(1)
joueur1.eliminer_pseudo("Pseudo1")
joueur1.ajouter_personnage(Personnage("Pseudo4"))

print(joueur1.get_personnage_numero(0).pseudo)  # Affiche "Pseudo2"