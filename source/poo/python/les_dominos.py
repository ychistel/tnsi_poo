from random import choice,randint

class Domino:
    """
    Objet avec 1 attribut valeur.
    Cet attribut est de type tuple représentant les points de chaque moitié du domino.
    Par exemple (3,5) est un domino.
    """
    def __init__(self,a,b):
        """
        Constructeur définissant l'attibut valeur de type tuple.
        L'attribut valeur est initialisé avec les deux valeurs a et b passées en paramètre. Ces valeurs sont des nombres entiers compris entre 0 et 6 inclus.
        On effectue un contrôle sur les paramètres.
        """
        pass
                
    def somme_points(self):
        """
        Méthode qui renvoie la somme des points du domino.
        """
        pass
    
    def __repr__(self):
        """
        Cette méthode renvoie une chaine de caractère représentant le domino. Par exemple, le domino de valeur (2,5) renvoie la chaine "[2|5]".
        Cette méthode est particulière car elle répond à l'utilisation de la fonction print.
        """
        pass

class Jeu:
    """
    Objet qui a un seul attribut dominos de type liste. La liste contient les 28 dominos qui sont des objets de la classe Domino.
    """
    def __init__(self):
        """
        Le constructeur définit l'attribut dominos de type liste. Cette liste contient les 28 objets dominos constituant le jeu.
        Attention un objet domino de valeur (2,5) est le même que l'objet domino de valeur (5,2). Il faut définir l'un ou l'autre.
        """
        pass

    def melanger(self):
        """
        Cette méthode mélange le jeu de dominos. Elle modifie l'ordre des dominos contenus dans la liste.
        """
        pass




class Joueur:
    """
    Un joueur contient jusqu'à 6 ou 7 dominos (selon le nombre de joueurs) pris parmi le jeu de dominos. Chaque joueur est identifié par un nom et sa liste de dominos.
    """
    def __init__(self,nom):
        """
        Constructeur qui définit les attributs nom et dominos.
        L'attribut nom est initialisé avec la valeur passée en paramètre.
        L'attribut age est initialisé avec la valeur passée en paramètre.
        L'attribut dominos est une liste vide.
        """
        pass
    
    def piocher(self,jeu):
        """
        Cette méthode pioche un domino parmi le jeu. Lorsque la pioche est faite, le domino est retiré du jeu passé en paramètre.
        """
        pass
    
                    
if __name__ == '__main__':
    # on crée le jeu de dominos affecté à la variable partie.
    pass

    # on crée les 3 joueurs J1? J2 ET J3
    pass

    # on distribue les dominos pour chaque joueur
    pass

    # on affiche les dominos de chaque joueur
    pass

    # On affiche la pioche
    pass

    # on cherche parmi les joueurs celui qui a le domino le plus fort. En cas d'égalité, c'est le plus jeune qui commence.
    pass
    