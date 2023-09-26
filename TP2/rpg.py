class Personnage:
    def __init__(self,pseudo: str, niveau: int=1, initiative: int=1, pv: int=1):
        self.__pseudo = pseudo
        self.__niveau = niveau
        self.__initiative = niveau
        self.__pv = niveau

    def __eq__(self, other):
        return self.__pseudo == other.pseudo

    @property
    def pseudo(self):
        return self.__pseudo

    @pseudo.setter
    def pseudo(self, ps):
        self.__pseudo = ps

    @property
    def initiative(self):
        return self.__initiative

    @initiative.setter
    def initiative(self, init):
        self.__initiative = init

    @property
    def niveau(self):
        return self.__niveau

    @niveau.setter
    def niveau(self, lvl):
        self.__niveau = lvl

    @property
    def pv(self):
        return self.__pv

    @pv.setter
    def pv(self, pv):
        self.__pv = pv

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
        while self.pv > 0 and opposant.pv > 0:
            self.attaque(opposant)
            print(f"Vos PV: {self.pv} \nPV opposant: {opposant.pv}")



    def soigner(self):
        """ méthode gérant le soin des personages """
        self.pv=self.niveau

    def degats(self) -> int:
        degats=self.niveau
        return degats


class Joueur:
    def __init__(self, nom: str, max_personnage: int):
        self.nom = nom
        self.max_personnage = max_personnage
        self.personnages = []

    def ajouter_personnage(self, personnage):
        if len(self.personnages) < self.max_personnage:
            self.personnages.append(personnage)
            print(f"Le personnage {personnage.pseudo} a été ajouté à la liste.")
        else:
            print("Le nombre maximum de personnages est atteint.")

    def get_personnage_numero(self, numero: int):
        if 0 <= numero < len(self.personnages):
            return self.personnages[numero]
        else:
            return None

    def get_personnage_pseudo(self, pseudo):
        for personnage in self.personnages:
            if personnage.pseudo == pseudo:
                return personnage
        return None

    def get_personnage(self, personnage):
        if personnage in self.personnages:
            return personnage
        else:
            return None

    def eliminer_numero(self, numero):
        if 0 <= numero < len(self.personnages):
            personnage_elimine = self.personnages.pop(numero)
            print(f"Le personnage {personnage_elimine.pseudo} a été éliminé.")
        else:
            print("Numéro de personnage invalide.")

    def eliminer_pseudo(self, pseudo):
        for personnage in self.personnages:
            if personnage.pseudo == pseudo:
                self.personnages.remove(personnage)
                print(f"Le personnage {personnage.pseudo} a été éliminé.")
                return
        print("Personnage introuvable.")

    def eliminer_personnage(self, personnage):
        if personnage in self.personnages:
            self.personnages.remove(personnage)
            print(f"Le personnage {personnage.pseudo} a été éliminé.")
        else:
            print("Personnage introuvable.")