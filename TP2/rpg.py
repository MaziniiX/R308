class Personnage:
    def __init__(self,pseudo: str, niveau: int=1, initiative: int=1, pv: int=1):
        self.pseudo=pseudo
        self.niveau=niveau
        self.initiative=niveau
        self.pv=niveau

    def attaque(self, opposant:'Personnage') -> None:
        """ méthode gérant un échange de coup
           :param opposant: l'autre personnage
           :type opposant: Personnage """
        if self.initiative > opposant.initiative:
            opposant.pv -= self.degats()
            if opposant.pv > 0:
                self.pv -= opposant.degats()
        elif self.initiative < opposant.initiative:
            self.pv -= opposant.degats()
            if self.pv > 0:
                opposant.pv -= self.degats()
        else:
            opposant.pv -= self.degats()
            self.pv -= opposant.degats()



    def combat(self, opposant):
        """ méthode gérant une succession d'attaque jusqu'a la mort d'un des deux personnages
            :param opposant: l'autre personnage
            :type opposant: Personnage """
        while True:
            self.attaque(opposant)
            if self.pv <=0:
                print("vous avez perdu")
            elif opposant.pv <=0:
                print("vous avez gagné")
            elif self.pv and opposant.pv <=0:
                print("vous etes tout les deux morts")
            break



    def soigner(self):
        """ méthode gérant le soin des personages """
        self.pv=self.niveau

    def degats(self) -> int:
        degats=self.niveau
        return degats


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

