Exercices pour expert
=====================

Exercice 1
----------

On importera le module ``pile.py`` qui est une implémentation de la ``pile`` en programmation orientée objet.

L'interface de la pile utilise les fonctions et les méthodes suivantes :

- Créer une pile vide : ``P=creer_pile()`` ou ``P = Pile()``;
- Empiler une valeur au sommet de la pile : ``P.empiler(x)``;
- Dépiler le sommet de la pile en renvoyant sa valeur ``y = P.depiler()``;
- Tester si la pile est vide : ``P.est_vide()``.

Une méthode d'affichage est aussi proposée en utilisant la fonction ``print``.

1. Créer une pile vide P.

2. Empiler dans la pile P un nombre aléatoire de valeurs (entre 5 et 10) choisies aléatoirement entre 1 et 20 (1 et 20 compris).

3. Écrire la fonction ``hauteur`` qui prend en argument une pile et renvoie le nombre d'éléments dans la pile. Celle-ci doit retrouver son état initial.

4. Écrire la fonction ``maximum`` qui prend en paramètre une pile et qui renvoie la valeur maximale de la pile. Si la pile contient plusieurs occurences de la valeur maximale, seule la première occurence sera renvoyée et supprimée de la pile.


Exercice 2
----------

On importera le module ``file.py`` qui est une implémentation de la ``file`` en programmation orientée objet.

L'interface de la file utilise les fonctions et les méthodes suivantes :

- Créer_file() qui crée une file vide : ``F = creer_file()`` ou ``F = File()``;
- Enfiler qui ajoute une valeur à la file : ``F.enfiler(valeur)``;
- Défiler qui supprime la tête de la file en renvoyant sa valeur : ``F.defiler()``;
- Est_vide() qui teste si la file est vide : ``F.est_vide()`` qui renvoie un booléen.

1. Créer 2 files vides F et G.
2. Enfiler un nombre aléatoire de valeurs (entre 10 et 20) dans la file F. Les valeurs sont des nombres aléatoires compris entre 1 et 100.
3. Créer un script qui enfile les nombres impairs de la file F dans la file G. La file F contiendra les nombres pairs à l'issue du script.

Exercice 3
----------

On importera les modules ``file.py`` et ``pile.py`` qui sont une implémentation de la ``file`` et de la ``pile`` en programmation orientée objet.

L'interface de la pile utilise les fonctions et les méthodes suivantes :

- Créer une pile vide : ``P=creer_pile()`` ou ``P = Pile()``;
- Empiler une valeur au sommet de la pile : ``P.empiler(x)``;
- Dépiler le sommet de la pile en renvoyant sa valeur ``y = P.depiler()``;
- Tester si la pile est vide : ``P.est_vide()``.

L'interface de la file utilise les fonctions et les méthodes suivantes :

- Créer_file() qui crée une file vide : ``F = creer_file()`` ou ``F = File()``;
- Enfiler qui ajoute une valeur à la file : ``F.enfiler(valeur)``;
- Défiler qui supprime la tête de la file en renvoyant sa valeur : ``F.defiler()``;
- Est_vide() qui teste si la file est vide : ``F.est_vide()`` qui renvoie un booléen.

1. Créer une file F contenant dans l'ordre les lettres de l'alphabét.
2. Créer la fonction ``inverse`` qui prend en paramètre une file et inverse les éléments de cette file. Vérifier en inversant les lettres de la file F.
3. Créer la fonction ``supprime`` qui prend en paramètre une file et qui renvoie la file en conserva,t uniquement les voyelles.

Exercice 4
----------

Exercice sur les files qui utilise le module ``file.py`` et qui traite de la conjecture de syracuse.

La Conjecture de syracuse appelée suite de Syracuse calcule une suite de nombres selon leur parité (pair ou impair). On utilisera une file pour stocker les valeurs de nos différentes suites de Syracuse. 

L'interface de la file utilise les fonctions et les méthodes suivantes :

- Créer_file() qui crée une file vide : ``F = creer_file()`` ou ``F = File()``;
- Enfiler qui ajoute une valeur à la file : ``F.enfiler(valeur)``;
- Défiler qui supprime la tête de la file en renvoyant sa valeur : ``F.defiler()``;
- Est_vide() qui teste si la file est vide : ``F.est_vide()`` qui renvoie un booléen.

.. _`wikipedia`: https://fr.wikipedia.org/wiki/Conjecture_de_Syracuse

Après avoir lu l'article sur `wikipedia`_, nous allons construire différentes fonctions en Python pour calculer les nombres de cette suite.

1. Importer la classe File et la fonction creer_file du module file.
2. Créer une file vide S qui stockera les nombres de notre suite de Syracuse.
3. Écrire la fonction ``syracuse`` de paramètre n, nombre entier, qui calcule les nombres de la suite de syracuse et enregistre les valeurs dans la file S.
4. On associe les nombres de syracuse à la trajectoire d'une feuille morte et on parle du vol de la suite. Trois valeurs symbolisent ce vol : le temps de vol, le temps de vol en altitude et l'altitude maximale.

   a. Écrire trois fonctions qui permettent d'obtenir ces trois valeurs. Attention, la file doit retrouver son état initial après les appels des fonctions.
   b. Créer un script qui permet de calculer les nombres de syracuse pour une valeur N donnée et affiche les trois valeurs du vol.

   .. admonition:: Exemple
   
      On calcule les termes de la suite pour N=129 et détermine les valeurs:

      - Le temps de vol pour N=129 est 121.
      - Le temps de vol en altitude pour N=129 est 2.
      - L'altitude maximale pour N=129 est 9232.

5. Représenter graphiquement les nombres de syracuse en important le module matplotlib et en utilisant la fonction graphik ci-dessous:

   .. code-block:: python

      # import du module avec alias plt
      from matplotlib import pyplot as plt

      # fonction qui permet de représenter graphiquement ces nombres:   
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

      #Appel pour afficher le graphique, on effectuera l'appel:    
          g=graphik(S)
          g.show() # <= inutile sur un notebook jupyter !

