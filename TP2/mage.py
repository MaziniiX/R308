import sys
import os
sys.path.append(os.path.join(__file__,"../"))
from rpg import Personnage

class Mage(Personnage):
    def __init__(self, pseudo : str,niveau: int = 1):
        super().__init__(pseudo,niveau)
        self.pv=niveau*5+10
        self.initiative=niveau*6+4
        self.mana=niveau*5

    def degats(self) -> int:
        """ méthode gérant les modification de dégats """
        if self.mana > 0:
            degats=self.niveau+3
            self.mana=self.mana-4
        else:
            degats=self.niveau
        return degats

    def soigner(self):
        """ méthode gérant le soin des personages """
        self.pv=self.niveau