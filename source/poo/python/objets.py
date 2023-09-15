from math import sqrt,pi
import matplotlib.pyplot as plt

class Point:

    def __init__(self,n,x,y):
        self.nom = n
        self.x = x
        self.y = y
        print("Point construit!")

class Segment:
    
    def __init__(self,pt1,pt2):
        self.ext1 = pt1
        self.ext2 = pt2
        print("Segment construit!")

    def longueur(self):
        d = sqrt((self.ext1.x-self.ext2.x)**2+(self.ext1.y-self.ext2.y)**2)
        return round(d,2)

class Cercle:

    def __init__(self,centre,r):
        self.centre = centre
        self.rayon = r
        print("Cercle construit")

    def aire(self):
        return pi*self.rayon**2
    
class Triangle:

    def __init__(self,a,b,c):
        self.cote_1 = Segment(a,b)
        self.cote_2 = Segment(b,c)
        self.cote_3 = Segment(c,a)
        print ("Triangle construit")

    def aire(self):
        # p est le demi périmètre du triangle
        p = (self.cote_1.longueur() + self.cote_2.longueur() + self.cote_3.longueur())/2
        # aire du triangle avec la formule de Héron
        return sqrt(p*(p-self.cote_1.longueur())*(p-self.cote_2.longueur())*(p-self.cote_3.longueur()))

class Graph:

    def __init__(self,*args) -> None:
        self.x_points = []
        self.y_points = []
        self.name_points = []
        self.segments = []
        self.cercles = []
        for valeur in args:
            if isinstance(valeur, Point):
                self.x_points.append(valeur.x)
                self.y_points.append(valeur.y)
                self.name_points.append(valeur.nom)
            elif isinstance(valeur, Segment):
                self.segments.append(valeur)
            elif isinstance(valeur,Cercle):
                self.cercles.append(valeur)
            elif isinstance(valeur,Triangle):
                self.segments.append(valeur.cote_1)
                self.segments.append(valeur.cote_2)
                self.segments.append(valeur.cote_3)

    def tracer_point(self):
        plt.plot(self.x_points, self.y_points,'o')
        for i in range(len(self.name_points)):
            plt.text(self.x_points[i]+0.1,self.y_points[i]+0.1,self.name_points[i])
    
    def tracer_segment(self):
        x = []
        y = []
        for segment in self.segments:
            x.append(segment.ext1.x)
            x.append(segment.ext2.x)
            y.append(segment.ext1.y)
            y.append(segment.ext2.y)
        plt.plot(x, y, marker='o')

    def tracer_cercle(self):
        for cercle in self.cercles:
            x,y = cercle.centre.x,cercle.centre.y
            circ = plt.Circle((x,y),cercle.rayon)
            plt.gca().add_patch(circ)

    def representer(self):
        #plt.axis('off')
        plt.axhline()
        plt.axvline()
        plt.axis('equal')
        self.tracer_point()
        self.tracer_segment()
        self.tracer_cercle()
        plt.show()

def affiche(point):
    print(f"Les coordonnées du point {point.nom} sont ({point.x},{point.y})")

def distance(pt1,pt2):
    d = sqrt((pt1.x-pt2.x)**2+(pt1.y-pt2.y)**2)
    return round(d,2)

if __name__ == '__main__':
    A = Point("A",1,2)
    affiche(A)
    B = Point("B",4,-3)
    affiche(B)
    C = Point("C",2,-2)
    AB = Segment(A,B)
    AC = Segment(A,C)
    BC = Segment(B,C)
    C1 = Cercle(A,2)
    C2 = Cercle(B,1)
    T = Triangle(A,B,C)
    #print(f"la longueur du segment AB est {AB.longueur()}")
    G = Graph(A,B,C,AB,AC,BC,C1,C2)
    G.representer()