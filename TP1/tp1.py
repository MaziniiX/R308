from Typing import Union
import sys
import math
"""
---------------------------------------
|           Classe Point              |
---------------------------------------
|  - x : float                        |
|  - y : float                        |
---------------------------------------
|  + Point():                         |
|  + Point(x:float, y:float):         |
---------------------------------------
|  + distance(x:float, y:float):float |
|  + distance(p:Point):               |
---------------------------------------
"""
class Point:
    def __init__(self, x:float=0.0, y:float=0.0):
        if isinstance(x,Union[int,float]) and isinstance(y,Union[int,float]):
            self.__x = x
            self.__y = y
        else:
            raise TypeError("erreur de type sur x ou y")

    def __str__(self) -> str:
        return f"Point[{self.__x};{self.__y}]"

    def distance(self, a, b):
        # Calcul de la distance entre le point actuel et un autre point (a, b)
        return math.sqrt((self.x - a) ** 2 + (self.y - b) ** 2)

    def distance_to(self, camarade):
        # Calcul de la distance entre le point actuel et un autre point (de type Point)
        return math.sqrt((self.x - camarade.x) ** 2 + (self.y - camarade.y) ** 2)

"""
-------------------------------------------
|           Classe Cercle                 |
-------------------------------------------
|  - centre : Point                       |
|  - rayon : float                        |
-------------------------------------------
|  + Cercle(rayon: float):                |
|  + Cercle(centre: Point, rayon: float): |
|  + diametre(): float                    |
|  + perimetre(): float                   |
|  + surface(): float                     |
|  + intersection(autre: Cercle): bool    |
-------------------------------------------
"""

class Cercle:
    def __init__(self, rayon, centre=Point()):
        self.rayon = rayon
        self.centre = centre

    def diametre(self):
        return 2 * self.rayon

    def perimetre(self):
        return 2 * math.pi * self.rayon

    def surface(self):
        return math.pi * self.rayon ** 2

    def intersection(self, cercle):
        distance_centres = self.centre.distance_to(cercle.centre)
        somme_rayons = self.rayon + cercle.rayon
        return distance_centres < somme_rayons



"""
---------   aggregation   ----------
| Point | <-------------- | Cercle |
---------                 ----------
"""