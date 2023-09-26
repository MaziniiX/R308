class Pokemon:
    def __init__(self, nom, poids):
        self.__nom = nom
        self.__poids = poids

    def calculer_vitesse(self):
        pass

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, nom):
        self.__nom = nom

    @property
    def poids(self):
        return self.__poids

    @poids.setter
    def poids(self, poids):
        self.__poids = poids

    def __str__(self):
        pass
