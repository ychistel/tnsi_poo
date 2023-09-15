class Nom_classe:
    # cette classe crée des objets de type Nom_classe

    pass





class Automobile:
    # classe Automobile pour construire des objets de type Automobile

    def __init__(self):        
        # constructeur de l'objet

        self.modele = "clio"
        self.nombre_portes = 3


class Automobile:
    # classe Automobile pour construire des objets de type Automobile

    def __init__(self,nom,n):
        # constructeur de l'objet avec paramètres

        self.modele = nom
        self.nombre_portes = n


class Automobile:
    # classe Automobile pour construire des objets de type Automobile

    def __init__(self,nom,n):
        # constructeur de l'objet avec paramètres

        self.modele = nom
        self.nombre_portes = n
        # v est la vitesse initiale égale à 0
        self.vitesse = 0 

    # méthode de l'objet
    def avancer(self):
        if self.vitesse > 0:
            return True
        else:
            return False



class automobile:
    # classe Automobile pour construire des objets de type Automobile

    def __init__(self,nom,n):
        # constructeur de l'objet avec paramètres

        self.modele = nom
        self.nombre_portes = n
        # v est la vitesse initiale égale à 0
        self.vitesse = 0 

    # méthode de l'objet
    def avancer(self):
        if self.vitesse > 0:
            return True
        else:
            return False
        
    def ralentir(self,v):
        if self.vitesse >= v:
            self.vitesse = self.vitesse - v
        else:
            self.vitesse = 0