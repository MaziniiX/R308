class Tasse:
    matiere:str="céramique"
    def __init__(self, couleur:str, contenance:int, marque:str):
        self.contenance = contenance
        self.marque = marque
        self.couleur = couleur

    def __str__(self):
        return f"la tasse de matière {Tasse.matiere}, de couleur {self.couleur} et de marque {self.marque} a une contenance de {self.contenance} ml"

    def contenu(self, boisson:str):
        self.boisson = boisson
        return f"et contient du {boisson}"

    def boire_tasse(self):
        del(self)
        
        


t=Tasse("bleu",50,"ikea")
b=t.contenu("café")
print(t,b)