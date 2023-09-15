from math import sqrt

class Point:

    def __init__(self,x,y):
        self.x = x # abscisse du point
        self.y = y # ordonnée du point
        print("Point construit!")
        
def affiche(point):
    print(f"Les coordonnées du point sont ({point.x},{point.y})")

def distance(pt1,pt2):
    d = sqrt((pt1.x-pt2.x)**2+(pt1.y-pt2.y)**2)
    return round(d,2)

class Segment:
    
    def __init__(self,pt1,pt2):
        self.ext1 = pt1
        self.ext2 = pt2
        print("Segment construit!")

if __name__ == '__main__':
    A = Point(1,2)
    affiche(A)
    B = Point(3,4)
    affiche(B)
    B.x=4
    B.y=-2
    affiche(B)
    print(f"la distance AB est {distance(A,B)}")