Exercices d'approfondissement
=============================


Exercice 1
----------

On reprend le travail effectué dans l'activité sur les classes ``Point`` et ``Segment``.

On propose de créer 2 nouvelles classes ``Cercle`` et ``Triangle``.

- La classe ``Cercle`` crée des objets dont les attributs sont un objet ``Point`` et un nombre pour le rayon. Lorsqu'on construit un objet de type ``Cercle``, le centre et le rayon sont passés en arguments.
- La classe ``Triangle`` crée des objets dont les attributs sont trois côtés définis comme objets ``Segment`` Lorsqu'un objet de type ``Triangle`` est construit, les trois points sommets sont passés en arguments.

#. Pour la classe ``Cercle``.

   a. Écrire le constructeur de la classe définissant les attributs ``centre`` et ``rayon``.
   b. Écrire la méthode ``aire`` qui calcule l'aire du cercle avec la formule :math:`\pi \times rayon^{2}`.

#. Pour la classe ``Triangle``.

   a. Écrire le constructeur de la classe définissant les attributs ``cote_1``, ``cote_2`` et ``cote_3``. On rappelle que ce sont trois points qui sont passés en argument lors de la construction d'un objet.
   b. La formule de Héron permet de calculer l'aire d'un triangle avec les longueurs des 3 côtés du triangle. On en donne la formule: :math:`\sqrt{p(p-a)(p-b)(p-c)}` où :math:`a`, :math:`b`, :math:`c` sont les longueurs des côtés du triangle et :math:`p` le demi-périmètre du triangle.

      Écrire la méthode ``aire`` qui renvoie l'aire d'un triangle calculée avec la méthode de Héron.


Exercice 2
----------

On définit l'objet ``Compte_bancaire`` dont voici l'interface :

- Attributs : ``solde`` et ``titulaire``
- Méthodes : ``est_positif``, ``crediter``, ``debiter``, ``virer_vers``, ``afficher`` ou ``__repr__``

1. Écrire la classe ``Compte_bancaire``, son constructeur ``__init__`` puis les différentes méthodes.

2. Tester en créant un compte bancaire **A** avec un solde de 1000 euros et un compte bancaire **B** avec un solde bancaire de 200 euros.

3. Effectuer un virement de 300 euros de A vers B.

4. Interdire tout virement si le solde du compte est négatif.


Exercice 3
----------

Le jeu de cartes peut être construit avec différentes structures de données Python. On se propose de créer un tel jeu avec deux classes. La classe ``Carte`` pour chaque carte du jeu et la classe ``Paquet`` qui sera composé de 52 objets de type Carte. 

.. image:: ../img/objet_carte.svg
   :align: center
   :width: 360px
   
On donne la structure globale de nos deux classes:

.. code:: python

   class Carte:
       
       # constructeur
       
       # valeur de la carte
       
       # couleur de la carte
       
   class Paquet:
   
       # constructeur
       
       # remplir un paquet
       
       # mélanger le paquet
       
       # tirer une carte en position donnée
       
Vous devez coder les 2 classes en prenant en compte les indications ci-dessous pour les méthodes.

1. Le constructeur de la classe ``Carte`` a 2 paramètres ``c`` et ``v`` correspondant à la couleur et à la valeur de la carte.

2. La méthode ``get_couleur`` renvoie la couleur de la carte, c'est à dire une valeur parmi ``coeur``, ``carreau``, ``pique`` et ``trèfle``. La valeur renvoyée est une chaine de caractères.

3. La méthode ``get_valeur`` renvoie la valeur de la carte. On distinguera les cas particuliers des cartes **as**, **valet**, **dame** et **roi**.

4. Le constructeur de la classe ``Paquet`` initialise l'attibut ``contenu`` avec une liste vide.

5. La méthode ``remplir`` ajoute à la liste ``contenu`` les 52 cartes du jeu. Chaque carte étant un objet de type Carte.

6. La méthode ``melanger`` se charge de mélanger de façon aléatoire le contenu du paquet de cartes.

7. La méthode ``get_carte_at`` prend en paramètre un entier *n* compris entre 1 et 52 (compris) et renvoie la carte qui se trouve en position *n* dans le paquet. Attention au décalage.

Vérifier que vos classes vous permettent:

- de fabriquer un paquet de carte
- d'afficher une carte choisie dans le paquet 


Exercice 4
----------

.. image:: ../img/jeu_dominos.jpg
   :align: center
   :width: 480
   
Le jeu de dominos est constitué de 28 pièces. Une pièce de domino est en deux parties. Chaque partie contient de 0 à 6 points. Lorsque les deux parties ont le même nombre de points, les dominos sont doubles. Il y a 7 doubles dans un jeu : du double 0 au double 6.

#. La classe Domino définit l'objet **domino** avec a un seul attribut ``valeur``. L'attribut est un tuple représentant les points de chaque moitié du domino.

   .. image:: ../img/classe_Domino_2.svg
      :align: center
      :width: 200

   Les méthodes de cette classe sont:

   -  Le constructeur ``__init__`` qui initialise l'attribut ``valeur`` avec un tuple dont les valeurs sont passées en paramètres.
   -  La méthode ``somme_points`` qui renvoie la somme des points du domino.
   -  La méthode ``__repr__`` qui affiche le domino, par exemple ``[a|b]``.

   On donne ci-dessous le code de la classe à compléter:

   .. literalinclude:: ../python/les_dominos.py
      :lines: 3-28

#. La classe ``Jeu`` a un seul attribut et 2 méthodes.

   L'attribut ``dominos`` est une liste contenant les 28 dominos du jeu. Chaque domino est un objet ``Domino``.
   
   Les méthodes de cette classe sont:

   - Le constructeur ``__init__`` initialise l'attribut ``dominos`` avec une liste dont les valeurs sont les 28 dominos du jeu.
   - La méthode mélange qui range dans un ordre aléatoire la liste des 28 dominos.
   
   .. image:: ../img/classe_JeuDomino_2.svg
      :align: center
      :width: 200

   On donne ci-dessous le code de la classe à compléter:

   .. literalinclude:: ../python/les_dominos.py
      :lines: 30-46

#. La classe ``Joueur`` a 3 attributs et 2 méthodes.

   - L'attribut ``nom`` contient le nom du joueur
   - L'attribut ``age`` contient l'age du joueur
   - L'attribut ``dominos`` est une liste qui contient les dominos du joueur

   Les méthodes de cette classe sont:

   - Le constructeur ``__init__`` initialise les attributs ``nom`` et ``age`` avec les valeurs passées en paramètres et l'attribut ``dominos`` avec une liste vide.
   - La méthode ``piocher`` ajoute un domino au joueur en le retirant de l'objet construit avec la classe ``Jeu``.

   .. image:: ../img/classe_Joueur_2.svg
      :align: center
      :width: 200

   On donne ci-dessous le code de la classe à compléter:

   .. literalinclude:: ../python/les_dominos.py
      :lines: 50-67
      
#. Le programme principal:

   - On crée un jeu de dominos
   - On crée 3 joueurs
   - Chaque joueur pioche chacun son tour un domino dans le jeu jusqu'à 7.
   - On affiche les dominos de chaque joueur et les dominos restant dans la pioche.
   - On détermine le joueur qui doit commencer la partie. 

   On donne les gandes lignes du programme principal ci-dessous:

   .. literalinclude:: ../python/les_dominos.py
      :lines: 70-87

   Compléter ce programme principal en remplaçant les ``pass`` par les lignes de code qui conviennent.


Exercice 5
----------

Les fractions sont des nombres dits rationnels de la forme :math:`\dfrac{a}{b}`. Le nombre :math:`a` est le **numérateur** et le nombre :math:`b` est le **dénominateur**. Ce sont des nombres entiers et :math:`b` est strictement positif.

On va définir une classe ``Fraction`` dans laquelle nous retrouverons différentes méthodes pour les calculs. La classe Fraction possède deux attributs : ``num`` et ``denom``.

1. Écrire le constructeur de cette classe. On prendra en compte le dénominateur strictement positif.
2. Ajouter une méthode ``__str__`` qui renvoie une chaine de caractères de la forme "a/b" ou simplement "a" lorsque le dénominateur est égal à 1.
3. Pour comparer deux nombres, on utilise les opérateurs ``==``, ``<`` ou ``>``. En python, ces opérateurs sont associés aux méthodes ``__eq__``, ``__lt__`` ou ``__gt__`` qui reçoivent une deuxième fraction en argument et renvoient un booléen.

   a. Créer dans la classe ``Fraction`` ces trois méthodes pour comparer deux objets de type ``Fraction``.
   b. Créer les fractions :math:`\dfrac{1}{2}` et :math:`\dfrac{3}{4}` puis effectuer des comparaisons.

4. Pour ajouter ou multiplier deux nombres, on utilise les opérateurs ``+`` et ``*``. En python, ces opérateurs sont associés aux méthodes ``__add__`` et ``__mul__`` qui reçoivent une deuxième fraction en argument et renvoient un résultat.

   a. Créer dans la classe ``Fraction`` ces deux méthodes de calcul entre deux objets de type ``Fraction``.
   b. Créer les fractions :math:`\dfrac{1}{2}` et :math:`\dfrac{3}{4}` puis effectuer les calculs.   


Exercice 6
----------

On va créer une classe Date pour représenter une date avec trois attributs jour, mois et annee.

1. Écrire son constructeur avec les paramètres j, m et a.
2. On peut créer une variable de classe qui sera utilisée dans la classe par différentes méthodes. L'appel de cette méthode se fera par ``nom de la classe.variable``.

   Créer une variable de classe mois de type liste contenant les douze mois de l'année. Cette variable sera accessible  avec l'appel ``Date.mois``.
   
3. Ajouter une méthode ``__str__`` qui renvoie une chaine de caractères de la forme "11 novembre 1918". Tester l'affichage avec la commande ``print``.

4. Ajouter une méthode ``__lt__`` qui permet de déterminer si une date d1 est antérieure à une date d2 en écrivant d1 < d2. La tester.

5. a. Modifier le constructeur avec des valeurs par défaut initialisées au 1 janvier 2000.

   b. Créer un objet Date, nommé ``ddn``, sans paramètres. Vérifier que les attributs de ``ddn`` ont pour valeurs la date du 1 janvier 2000.

   c. Modifier les attributs ``ddn`` avec les dates de votre anniversaire.
 
6. Dans la question précédente, vous avez remarqué qu'il est possible de modifier la valeur des attributs d'un objet. Cela peut poser des problèmes surtout lorsqu'on a des attributs dont les valeurs ne doivent pas être accessibles.

   Il est possible d'interdire l'accès aux attributs en les cachant. Il suffit d'ajouter un double souligné devant le nom de l'attribut : ``self.__attribut``.

   a. Modifier dans le constructeur les attributs jour, mois et annee pour qu'ils soient cachés. 
      
      Penser aussi à modifier les méthodes qui les utilisent.
   
   b. Vérifier qu'il n'est plus possible de modifier les valeurs d'une date une fois créée.

7. Pour accéder aux attributs cachés et les modifier, on peut créer des méthodes particulières appelées **accesseurs** et **mutateurs**.

   On définit pour l'attribut caché jour, l'accesseur ``get_jour`` et le mutateur ``set_jour`` de la manière suivante:
   
   .. image:: ../img/poo1.jpg
      :align: center
      :width: 560px
      
   a. Ajouter ces deux méthodes dans la classe ``Date`` et vérifier que vous pouvez afficher et modifier le jour d'une date.
   b. Ajouter les accesseurs et les mutateurs pour le mois et l'année.
   c. Vérifier, après avoir créé une date ``ddn`` sans paramètres, que vous pouvez la modifier par votre date de naissance.
