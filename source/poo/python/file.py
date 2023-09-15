"""
Module : implémentation d'une File par des listes chainées en POO
Objets
- Maillon : permet de construire chaque élément de la File
- File : permet de construire une liste chainée créant une file.
Fonctions
- creer_file : pour construire une file vide.
"""

class Maillon:
    def __init__(self, valeur=None, suivant=None):
        self.valeur = valeur
        self.suivant = suivant
        
    def __repr__(self):
        if self.suivant is None:
            return str(self.valeur) 
        else:
            return str(self.valeur) + " < " + str(self.suivant)


class File:
    
    """
    type : objet de type liste chainée
    attributs :
    - maillon : objet Maillon ou None si vide
    méthodes:
    - constructeur __init__
    - enfiler : ajoute un objet Cellule à l'objet File
    - defiler : renvoie la tête de la file en le supprimant
    - est_vide : renvoie un booléen (True, False) indiquant si la File est vide
    - tete : renvoie la tete de file sans l'enlever
    - __repr__ pour afficher le contenu de la file (méthode non définie dans l'interface)
    """
    
    def __init__(self):
        self.maillon = None
        self.last = None
        
    def est_vide(self):
        return self.maillon == None
        
    def defiler(self):
         if not self.est_vide():
            maillon = self.maillon
            tete = maillon.valeur
            self.maillon = maillon.suivant
            return tete
            
    def enfiler(self, element):
        maillon = Maillon(element)
        if self.maillon == None:
            self.last = maillon
            self.maillon = maillon
        else:
            self.last.suivant = maillon
            self.last = maillon
        
    def tete(self):
        if not self.est_vide():
            return self.maillon.valeur
   
    def __repr__(self):
        return str(self.maillon)

def creer_file():
    return File()


if __name__=='__main__':
    F=creer_file()
    print("La file est vide:",F.est_vide())
    print("On enfile 3, 7, 9 et 11")
    F.enfiler(3)
    F.enfiler(7)
    F.enfiler(9)
    F.enfiler(11)
    print("La file F contient :",F)
    print("La tête de la file F est:",F.tete())
    print("On defile:")
    F.defiler()
    print("La file F contient :",F)
    print("La file F est vide:",F.est_vide())
    print("On defile entièrement la file F")
    while not F.est_vide():
        F.defiler()
    print("La file F est vide :",F.est_vide())
