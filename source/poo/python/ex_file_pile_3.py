from file import *
from pile import *

F = creer_file()
for i in range(140):
    F.enfiler(chr(40+i))
    
def inverser(file):
    pile = creer_pile()
    while not file.est_vide():
        pile.empiler(file.defiler())
    while not pile.est_vide():
        file.enfiler(pile.depiler())
    return file

def supprime(file):
    voyelle = ['a','e','i','o','u','y']
    tmp = creer_file()
    while not file.est_vide():
        lettre = file.defiler()
        if lettre in voyelle:
            tmp.enfiler(lettre)
    return inverser(tmp)

print(F)
F = supprime(F)
print(F)