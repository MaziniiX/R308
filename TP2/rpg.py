class Personnage:
    def __init__(self,pseudo: str, niveau: int=1, initiative: int=1, pv: int=1):
        self.pseudo=pseudo
        self.niveau=niveau
        self.iniative=niveau
        self.pv=niveau

    def attaque(self, opposant:'Personnage') -> None:
        """ méthode gérant un échange de coup
           :param opposant: l'autre personnage
           :type opposant: Personnage """
        if self.initiative > opposant.iniative:
            opposant.pv -= self.niveau
            if opposant.pv > 0:
                self.pv -= opposant.niveau
        elif self.initiative < opposant.initiative:
            self.pv -= opposant.niveau
            if self.pv > 0:
                opposant.pv -= self.niveau
        else:
            opposant.pv -= self.niveau
            self.pv -= opposant.niveau



    def combat(self, opposant):
        """ méthode gérant une succession d'attaque jusqu'a la mort d'un des deux personnages
            :param opposant: l'autre personnage
            :type opposant: Personnage """
        while self.pv >= 0 or opposant.pv >= 0:
            if self.initiative > opposant.iniative:
                opposant.pv -= self.niveau
                if opposant.pv > 0:
                    self.pv -= opposant.niveau
            elif self.initiative < opposant.initiative:
                self.pv -= opposant.niveau
                if self.pv > 0:
                    opposant.pv -= self.niveau
            else:
                opposant.pv -= self.niveau
                self.pv -= opposant.niveau



    def soigner(self):
        """ méthode gérant le soin des personages """
        self.pv=self.niveau

class Guerrier(Personnage):
    def __init__(self, pseudo: str, niveau: int=1):
        super().__init__(pseudo)