from time import sleep
from random import choice,randint

class Domino:
    
    def __init__(self,a,b):
        self.valeur = [a,b]
        
    def retourner(self):
        if self.valeur != []:
            a,b = self.valeur
            self.valeur[0] = b
            self.valeur[1] = a
        
    def somme_points(self):
        a,b = self.valeur
        return a+b
    
    def difference_points(self):
        a,b = self.valeur
        return abs(a-b)
    
    def __repr__(self):
        a,b = self.valeur
        domino = "[%s|%s]" % (a,b)
        return domino

class JeuDomino:
    
    def __init__(self):
        self.dominos = [Domino(i,j) for i in range(7) for j in range(i,7)]
        
    def jouable(self,tapis,joueurs):
        if self.dominos == []:
            return False
        else:
            jouable = True
            for joueur in joueurs:
                if joueur.dominos == []:
                    return False
                else:
                    if joueur.jouable(tapis) != []:
                        jouable = jouable or True
                    else:
                        jouable = jouable or False
            return jouable
                    

class Joueur:
    
    def __init__(self,nom):
        self.nom = nom
        self.dominos = []
        self.dominos_jouables = []
        self.somme_points = 0
    
    def est_vide(self):
        return self.dominos == []
        
    def calculer_points(self):
        if not self.est_vide():
            for domino in self.dominos:
                self.somme_points += domino.somme_points()
        return self.somme_points
    
    def piocher(self,jeu):
        domino = []
        if jeu.dominos != []:
            domino = choice(jeu.dominos)
            self.dominos.append(domino)
            jeu.dominos.remove(domino)
        return domino
    
    def poser(self,tapis,domino):
        if not tapis.est_vide():
            domino_left = tapis.a_gauche()
            domino_right = tapis.a_droite()
            
            if domino_left.valeur[0] == domino.valeur[1]:
                tapis.inserer_gauche(domino)
                self.dominos.remove(domino)
            elif domino_right.valeur[1] == domino.valeur[0]:
                tapis.inserer_droite(domino)
                self.dominos.remove(domino)
        else:
            tapis.dominos.append(domino)
            self.dominos.remove(domino)
    
    def jouable(self,tapis):
        self.dominos_jouables = []
        if not tapis.est_vide():
            domino_left = tapis.a_gauche()
            domino_right = tapis.a_droite()
            for domino in self.dominos:
                if domino_left.valeur[0] == domino.valeur[0] :
                    domino.retourner()
                    self.dominos_jouables.append(domino)
                elif domino_left.valeur[0] == domino.valeur[1] :
                    self.dominos_jouables.append(domino)
                elif domino_right.valeur[1] == domino.valeur[0] :
                    self.dominos_jouables.append(domino)
                elif domino_right.valeur[1] == domino.valeur[1] :
                    domino.retourner()
                    self.dominos_jouables.append(domino)
        return self.dominos_jouables

    def domino_fort(self,dominos):
        """
        Renvoie le domino qui a la plus forte valeur:
        - plus grande somme de points
        - plus petite différence de points en cas d'égalité sur la somme
        """
        if not dominos == []:
            s = dominos[0].somme_points()
            d = dominos[0].difference_points()
            position = 0
            i = 0
            for domino in dominos:
                if  s < domino.somme_points() :
                    s = domino.somme_points()
                    d = domino.difference_points()
                    position = i
                elif s == domino.somme_points() :
                    if d > domino.difference_points():
                        s = domino.somme_points()
                        d = domino.difference_points()
                        position = i
                i += 1
            return dominos[position]

class Tapis:
    
    def __init__(self):
        self.dominos = []
        
    def est_vide(self):
        return self.dominos == []
    
    def a_gauche(self):
        """
        Renvoie le domino le plus à gauche du tapis
        """
        if not self.est_vide():
            return self.dominos[0]
        
    def a_droite(self):
        """
        Renvoie le domino le plus à droite du tapis
        """
        if not self.est_vide():
            return self.dominos[-1]
        
    def inserer_gauche(self,domino):
        liste_domino = []
        liste_domino.append(domino)
        self.dominos = liste_domino + self.dominos
        return self.dominos
    
    def inserer_droite(self,domino):
        liste_domino = []
        liste_domino.append(domino)
        self.dominos = self.dominos + liste_domino
        return self.dominos
                    
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
    
    while partie_jouable:
        print(joueur.nom," joue ! il a les dominos :",joueur.dominos)
        dominos_jouables = joueur.jouable(tapis)
        print(joueur.nom,"peut jouer :",dominos_jouables)
        if joueur.dominos_jouables != []:
            print(joueur.nom,"joue le domino ",joueur.domino_fort(joueur.dominos_jouables))
            joueur.poser(tapis,joueur.domino_fort(joueur.dominos_jouables))
            print("tapis:",tapis.dominos)
        else:
            print(joueur.nom," ne peut pas jouer!")
            if partie.dominos != []:
                pioche = joueur.piocher(partie)
                print(joueur.nom," a pioché ",pioche,"ses dominos: ",joueur.dominos)
            else:
                print(joueur.nom,"passe son tour!")
        partie_jouable = partie.jouable(tapis,joueurs)
        if partie_jouable:
            i = joueurs.index(joueur)
            if i < len(joueurs)-1:
                joueur = joueurs[i+1]
            else:
                joueur = joueurs[0]
        sleep(1)

    # Fin de partie
    vainqueur = joueurs[0]
    for joueur in joueurs:
        if joueur.est_vide():
            vainqueur = joueur
            #print(vainqueur.nom," a gagné la partie.")
            break
        else:
            joueur.calculer_points()
            print(joueur.nom," a encore les dominos ",joueur.dominos,"pour un total de ",joueur.somme_points,"points.") 
            if joueur.somme_points < vainqueur.somme_points:
                vainqueur = joueur
    print(vainqueur.nom,"a gagné la partie avec ",vainqueur.somme_points,"points")
    print("Tapis:",tapis.dominos)



