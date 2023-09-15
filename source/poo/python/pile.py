"""
Module : implémentation d'une Pile comme les listes chainées en POO
Objets
- Maillon : permet de construire chaque élément de la Pile
- Pile : permet de construire une liste chainée créant une pile.
Fonctions
- creer_pile : pour construire une pile vide.
"""

class Maillon:
    """
    type : objet
    attributs : 
    - elt qui contient la valeur passée en argument
    - suivant : None par défaut ou un objet Cellule pour construire une liste chainée.
    méthodes:
    - constructeur __init__
    """
    def __init__(self, valeur=None, suivant=None):
        self.valeur = valeur
        self.suivant = suivant
        
    def __repr__(self):
        if self.suivant is None:
            return "[ "+str(self.valeur)
        else:
            return str(self.suivant) + " [ " +str(self.valeur)
        
class Pile:
    """
    type : objet de type liste chainée
    attributs :
    - taille : nombre entier indiquant le nombre de Cellules
    - sommet : valeur au sommet de la pile
    méthodes:
    - constructeur __init__
    - empiler : ajoute un objet Cellule à l'objet Pile
    - depiler : renvoie la tête de la Pile en le supprimant
    - sommet : renvoie la valeur du sommet de la Pile sans la dépiler
    - est_vide : renvoie un booléen (True, False) indiquant si la Pile est vide
    - __repr__ pour afficher le contenu de la pile (méthode non définie dans l'interface)
    """
    
    def __init__(self):
        self.maillon = None
        
    def est_vide(self):
        return self.maillon == None
        
    def empiler(self, element):
        # on crée un nouveau maillon avec la valeur element : [element]->[]
        nv_maillon = Maillon(element)
        # on pointe le maillon sur la liste (attribut maillon) : [element]->[*]->[*]->... comme L->[*]->[*]->...
        nv_maillon.suivant = self.maillon
        # on pointe la liste sur le nouveau maillon : L->[element]->...
        self.maillon = nv_maillon
        
    def depiler(self):
        maillon = self.maillon
        if not self.est_vide():
            sommet = maillon.valeur
            self.maillon = maillon.suivant
            return sommet
            
     
    def sommet(self):
        if not self.est_vide():
            return self.maillon.valeur
        
    
    def __repr__(self):
        if self.maillon == None:
            return "["
        else:
            return str(self.maillon)

def creer_pile():
    return Pile()


if __name__=='__main__':
    P=creer_pile()
    print("La pile P est vide:",P.est_vide())
    print("On empile 3 et 7")
    P.empiler(3)
    P.empiler(7)
    print(P)
    print("On empile 9")
    P.empiler(9)
    print(P)
    print("La pile P est vide:",P.est_vide())
    print("Le sommet de la pile est:",P.sommet())
    print("On dépile toute la pile!")
    while not P.est_vide():
        P.depiler()
    print("La pile est vide:",P)