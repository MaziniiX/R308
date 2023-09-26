from pokemon import Pokemon

class PokemonSportif(Pokemon):
    def __init__(self, nom, poids, nombre_pattes, taille, frequence_cardiaque):
        super().__init__(nom, poids)
        self.__nombre_pattes = nombre_pattes
        self.__taille = taille
        self.__frequence_cardiaque = frequence_cardiaque

    def calculer_vitesse(self):
        return (self.poids * 3) / (self.__taille * self.__frequence_cardiaque)

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
    def frequence_cardiaque(self):
        return self.__frequence_cardiaque

    @frequence_cardiaque.setter
    def frequence_cardiaque(self, frequence_cardiaque):
        self.__frequence_cardiaque = frequence_cardiaque

    def __str__(self):
        return f"Je suis le pokémon {self.nom} mon poids est de {self.poids} kg, ma vitesse est de {self.calculer_vitesse()} km/h, j'ai {self.__nombre_pattes} pattes, ma taille est de {self.__taille} m, ma fréquence cardiaque est de {self.__frequence_cardiaque} pulsations à la minute."
