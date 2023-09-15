class Cellule:
    def __init__(self, valeur=None, suivant=None):
        self.valeur = valeur
        self.suivant = suivant
        
    def __repr__(self):
        return "("+str(self.valeur)+"," +str(self.suivant)+")"

class Liste:
    def __init__(self):
        self.cellule = None

    def est_vide(self):
        return self.cellule == None
    
    def insere_en_tete(self,element):
        self.cellule = Cellule(element,self.cellule)
        
    def insere_en_fin(self,element): 
        nouvelle_cellule=Cellule(element,None)
        if self.est_vide():
            self.cellule=nouvelle_cellule
        else:
            cellule_courante=self.cellule
            while cellule_courante.suivant != None:
                cellule_courante = cellule_courante.suivant
            cellule_courante.suivant = nouvelle_cellule
        
    def tete(self):
        if not self.est_vide():
            return self.cellule.valeur

    def queue(self):
        subList = None
        if not self.est_vide():
            subList = Liste()
            subList.cellule = self.cellule.suivant
        return subList
    
    def __repr__(self):
        if self.est_vide():
            return "[]"
        else:
            return "["+str(self.tete())+"]->"+str(self.queue())

def creer_liste_chaine():
    return Liste()

L=creer_liste_chaine()
L.insere_en_tete(7)
L.insere_en_tete(4)
L.insere_en_tete(3)
L.insere_en_tete(2)
L.insere_en_fin(9)
L.insere_en_fin(12)
L.insere_en_tete(1)
print(L)