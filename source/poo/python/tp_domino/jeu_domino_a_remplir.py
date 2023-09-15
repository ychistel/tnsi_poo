from random import choice,randint

class Domino:
    
    def __init__(self,a,b):
        self.valeur = ...
        
    def retourner(self):
        pass
        
    def somme_points(self):
        pass
    
    def difference_points(self):
        pass
    
    def __repr__(self):
        pass

class JeuDomino:
    
    def __init__(self):
        self.dominos = ...
        
    def jouable(self,tapis,joueurs):
        pass
                    
class Joueur:
    
    def __init__(self,nom):
        self.nom = ...
        self.dominos = ...
        self.dominos_jouables = ...
        self.somme_points = 0
    
    def est_vide(self):
        pass
        
    def calculer_points(self):
        pass
    
    def piocher(self,jeu):
        pass
    
    def poser(self,tapis,domino):
        pass
    
    def jouable(self,tapis):
        pass

    def domino_fort(self,dominos):
        pass

class Tapis:
    
    def __init__(self):
        self.dominos = ...
        
    def est_vide(self):
        pass
    
    def a_gauche(self):
        pass
        
    def a_droite(self):
        pass
        
    def inserer_gauche(self,domino):
        pass
    
    def inserer_droite(self,domino):
        pass
                    
if __name__ == '__main__':
    partie = JeuDomino()
    tapis = Tapis()
    J1 = Joueur('Bob')
    J2 = Joueur('Alice')
    joueurs = [J1,J2]

    # on distribue les dominos
    for i in range(7):
        J1.piocher(partie)
        J2.piocher(partie)

    # début du jeu
    print(J1.nom,"joue et pose le domino :",J1.domino_fort(J1.dominos))
    J1.poser(tapis,J1.domino_fort(J1.dominos))
    print("Tapis:",tapis.dominos)
    joueur = J2
    
    partie_jouable = True
    
    while partie.jouable(tapis,joueurs):
        print(joueur.nom," joue ! ses dominos ",joueur.dominos)
        dominos_jouables = joueur.jouable(tapis)
        print(dominos_jouables)
        if joueur.dominos_jouables != []:
            joueur.poser(tapis,joueur.domino_fort(joueur.dominos_jouables))
            print("tapis:",tapis.dominos)
        else:
            print(joueur.nom," ne peut pas jouer!")
            if partie.dominos != []:
                pioche = joueur.piocher(partie)
                print(joueur.nom," a pioché ",pioche)
            else:
                print(joueur.nom,"passe son tour!")
        if joueur == J1:
            joueur = J2            
        else:
            joueur = J1

    # Fin de partie
    vainqueur = joueurs[0]
    for joueur in joueurs:
        if joueur.est_vide():
            print(joueur.nom," a gagné la partie.")
            break
        else:
            joueur.calculer_points()
            print(joueur.nom," a encore les dominos ",joueur.dominos,"pour un total de ",joueur.somme_points,"points.") 
            if joueur.somme_points < vainqueur.somme_points:
                vainqueur = joueur
            print(vainqueur.nom,"a gagné la partie avec ",vainqueur.somme_points,"points")
            print("Tapis:",tapis.dominos)
