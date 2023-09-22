import sys
import os
sys.path.append(os.path.join(__file__,"../"))
from rpg import Personnage
class Guerrier(Personnage):
    def __init__(self, pseudo : str,niveau: int = 1):
        super().__init__(pseudo,niveau)
        self.pv=niveau*8+4
        self.initiative=niveau*4+6

    def degats(self) -> int:
        """ méthode gérant les modification de dégats """
        degats=self.niveau*2
        return degats

    def soigner(self):
        """ méthode gérant le soin des personages """
        self.pv=self.niveau