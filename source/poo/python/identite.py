class Identite:

    def __init__(self,nom,age,jeu,sp,ins):
        self.nom = nom
        self.age = age
        self.jeu = jeu
        self.sport = sp
        self.instrument = ins
        print("objet construit")

    def afficher(self):
        msg = self.nom + '\n'
        msg = msg + "- âge : " + str(self.age) + '\n'
        msg = msg + "- jeu : " + self.jeu + '\n'
        msg = msg + "- sport : " + self.sport + '\n'
        msg = msg + "- instrument : " + self.instrument + '\n'
        print(msg)

def age_moyen(liste_objets):
    m = 0
    for obj in liste_objets:
        m += obj.age
    return m/len(liste_objets)

p_1 = Identite('Alice',9,'cartes','course à pied','piano')
p_2 = Identite('Bob',7,'quilles','natation','pipo')
p_3 = Identite('Carlo',75,'fléchettes','kayak','guitare')
print(f"Age moyen : {age_moyen([p_1,p_2,p_3])}")
p_1.afficher()
p_2.afficher()
p_3.afficher()
