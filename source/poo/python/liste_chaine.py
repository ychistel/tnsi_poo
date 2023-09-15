"""
Module : implémentation d'une liste chainé en POO
Objets
- Maillon : permet de construire chaque élément de la liste chainée
- Liste : permet de construire une liste chainée avec des maillons.
Fonctions
- creer_file : pour construire une liste chainée vide vide.
"""

class Maillon:
    def __init__(self, valeur=None, suivant=None):
        self.valeur = valeur
        self.suivant = suivant
        
    def __repr__(self):
        if self.suivant is None:
            return "["+str(self.valeur)+"]->" +"[]"
        else:
            return "["+str(self.valeur)+"]->" +str(self.suivant)

class Liste:
    
    """
    type : objet de type liste chainée
    attributs :
    - maillon : objet Maillon ou None si vide
    - last : dernier maillon de la liste chainée (premier inséré)
    méthodes:
    - constructeur __init__
    - inserer : ajoute un élément comme objet Maillon
    - ajouter_fin : ajoute un élément en fin de liste, last prend comme nouvelle valeur
    le maillon créé avec cet élément
    - est_vide : renvoie un booléen (True, False) indiquant si la File est vide
    - tete : renvoie la tete de la liste chainée sans l'enlever
    - __repr__ pour afficher le contenu de la liste chainée.
    """
    
    def __init__(self):
        self.maillon = None
        
        # on ajoute l'attribut last
        self.last = None
        
    def est_vide(self):
        return self.maillon == None
        
    def inserer(self, element):
        # on crée un nouveau maillon avec la valeur element : [element]->[]
        nv_maillon = Maillon(element)
        # on pointe le maillon sur la liste (attribut maillon) : [element]->[*]->[*]->... comme L->[*]->[*]->...
        nv_maillon.suivant = self.maillon
        # on pointe la liste sur le nouveau maillon : L->[element]->...
        self.maillon = nv_maillon       
        # puisqu'un élément est inséré, on modifie la valeur de last si il n'en a pas.
        if self.last == None:
            self.last = nv_maillon
            
    def ajouter_fin(self, element):
        dernier_maillon = Maillon(element)
        self.last.suivant = dernier_maillon
        self.last = dernier_maillon
        
    def tete(self):
        if not self.est_vide():
            return self.maillon.valeur
        
    def queue(self):
        # on crée une nouvelle liste qui sera la queue. La queue est une liste!
        queue = Liste()
        if not self.est_vide():
            queue.maillon = self.maillon.suivant
        return queue
    
    def __repr__(self):
        if self.maillon == None:
            return "[]"
        else:
            return str(self.maillon)

def creer_liste():
    return Liste()

if __name__ == '__main__':
    L = creer_liste()
    print("La liste L est vide :",L.est_vide())
    L.inserer('a')
    L.inserer('e')
    L.inserer('i')
    L.inserer('o')
    L.inserer('u')
    print(L)
    L.ajouter_fin('y')
    print(L)
