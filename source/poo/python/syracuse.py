from file import *
#from matplotlib import pyplot as plt

S=creer_file()

def syracuse(n):
    S.enfiler(n)
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            S.enfiler(n)
        else:
            n = 3*n + 1
            S.enfiler(n)


def temps_de_vol(file):
    tdv = 0
    x = file.defiler()
    while x != 1:
        file.enfiler(x)
        tdv += 1
        x = file.defiler()
    file.enfiler(x)
    return tdv


def temps_de_vol_altitude(file):
    tdva = 0
    n = file.defiler()
    file.enfiler(n)
    x = file.defiler()
    while x > n:
        tdva += 1
        file.enfiler(x)
        x = file.defiler()
    while x != 1:
        file.enfiler(x)
        x = file.defiler()
    file.enfiler(x)
    return tdva
            
def altitude_maximale(file):
    h = file.defiler()
    file.enfiler(h)
    x = file.defiler()
    while x != 1:
        if x > h:
            h = x
        file.enfiler(x)
        x = file.defiler()
    file.enfiler(x)
    return h

def graphik(file):
    if not file.est_vide():
        y = file.defiler()
        file.enfiler(y)
    n=1
    Y=[y]
    while y != 1:
        y = file.defiler()
        Y.append(y)
        n += 1
        file.enfiler(y)
    file.enfiler(y)
    X=[i for i in range(n)]
    plt.plot(X,Y)
    return plt

if __name__ == '__main__':
    N=129
    syracuse(N)
    print(S)
    print("Le temps de vol pour N=%s est %s." % (N,temps_de_vol(S)))
    print("Le temps de vol en altitude pour N=%s est %s." % (N,temps_de_vol_altitude(S)))
    print("L'altitude maximale pour N=%s est %s." % (N,altitude_maximale(S)))
    #g=graphik(S)
    #g.show()

