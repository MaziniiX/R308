from pokemon import Pokemon

class PokemonCasanier(Pokemon):
    def __init__(self, nom, poids, nombre_pattes, taille, heures_tele):
        super().__init__(nom, poids)
        self.__nombre_pattes = nombre_pattes
        self.__taille = taille
        self.__heures_tele = heures_tele

    def calculer_vitesse(self):
        return (self.poids * 3) / (self.__taille * self.__heures_tele)

    @property
    def nombre_pattes(self):
        return self.__nombre_pattes

    @nombre_pattes.setter
    def nombre_pattes(self, nombre_pattes):
        self.__nombre_pattes = nombre_pattes

    @property
    def taille(self):
        return self.__taille

    @taille.setter
    def taille(self, taille):
        self.__taille = taille

    @property
    def heures_tele(self):
        return self.__heures_tele

    @heures_tele.setter
    def heures_tele(self, heures_tele):
        self.__heures_tele = heures_tele

    def __str__(self):
        return f"Je suis le pokémon {self.nom} mon poids est de {self.poids} kg, ma vitesse est de {self.calculer_vitesse()} km/h, j'ai {self.__nombre_pattes} pattes, ma taille est de {self.__taille} m, je regarde la télé {self.__heures_tele}h par jour."
