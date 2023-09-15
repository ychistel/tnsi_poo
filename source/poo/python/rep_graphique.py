import matplotlib.pyplot as plt
from math import sqrt

"""
class Point:
    pass

class Segment:
    pass

class Cercle:
    pass
"""

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
        plt.axhline()
        plt.axvline()
        plt.axis('equal')
        self.tracer_point()
        self.tracer_segment()
        self.tracer_cercle()
        plt.show()


