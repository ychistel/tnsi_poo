class Personne:

    def __init__(self,n,a,h):
        self.nom = n
        self.age = a
        if h != '':
            self.hobby = h
        else:
            self.hobby = 'aucun'