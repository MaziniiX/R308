def pgn (a:int,b:int):
    if a > b:
        print("Le 1er nombre est le plus grand des deux")
    else:
        print("Le 1er nombre est le plus grand des deux")

#pgn(a,b)
#a=int(input())
#b=int(input())

def seuil (a:int,b:int=10):
    if a<=b:
        print("le nombre ne depasse pas le seuil")
    else:
        print("le nombre depasse le seuil")

#seuil(a,b)

#a=int(input())
#b=int(input())

def pgv(liste):
    liste.sort()
    print(liste[-1])

#pgv(liste)

#liste=[1,59,9,52,3]

def nli(l,s:int=3):
    if len(l)<=s:
        print(len(l))
    else:
        print("la liste est trop grande")

#l=[1,2,3]
#s=2

#nli(l,s)

def dico(a="|",d={"a":1,"b":2,"c":3,"d":4,"e":5}):
    for v in d:
        print(a,d[v],a)

#d={"a":1,"b":2,"c":3,"d":4,"e":5}
dico()
