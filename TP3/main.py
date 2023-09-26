from sportif import PokemonSportif
from casanier import PokemonCasanier
from mer import PokemonMer
from croisiere import PokemonCroisiere

# Création de différents Pokémon
pikachu = PokemonSportif("Pikachu", 18, 2, 0.85, 120)
salameche = PokemonCasanier("Salameche", 12, 2, 0.65, 8)
rondoudou = PokemonMer("Rondoudou", 45, 2)
bulbizarre = PokemonCroisiere("Bulbizarre", 15, 3)

# Affichage des caractéristiques de chaque Pokémon
print("Caractéristiques des Pokémons :")
print("-" * 30)
print(str(pikachu))
print(str(salameche))
print(str(rondoudou))
print(str(bulbizarre))
