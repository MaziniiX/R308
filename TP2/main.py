import sys
import os
sys.path.append(os.path.join(__file__,"../"))
import rpg as p
opposant=p.Personnage("j2",4)
p1=p.Personnage("j1",4)
p1.combat(opposant)
