from pokemon import Pokemon

class PokemonMer(Pokemon):
    def __init__(self, nom, poids, nombre_nageoires):
        super().__init__(nom, poids)
        self.__nombre_nageoires = nombre_nageoires

    def calculer_vitesse(self):
        return self.poids / (25 * self.__nombre_nageoires)

    @property
    def nombre_nageoires(self):
        return self.__nombre_nageoires

    @nombre_nageoires.setter
    def nombre_nageoires(self, nombre_nageoires):
        self.__nombre_nageoires = nombre_nageoires

    def __str__(self):
        return f"Je suis le pokémon {self.nom} mon poids est de {self.poids} kg, ma vitesse est de {self.calculer_vitesse()} km/h, j'ai {self.__nombre_nageoires} nageoires."
