Exercices de base
==================

Exercice 1
----------

On définit un objet avec la classe ``Fruit`` en Python:

.. literalinclude:: ../python/fruit.py
   :lines: 1-7

#. Quels sont les attributs et leurs types définis dans la classe ``Fruit``?
#. On instancie un premier objet ``a_1 = Fruit()``. 

   a. Quelles sont les valeurs des attributs de l'objet ``a_1`` ?
   b. Quelle est l'instruction Python qui affiche la masse de l'objet ``a_1``?

#. L'objet ``a_1`` représente 1 kg de pommes au prix de 3,20 euros. Quelles instructions Python modifient l'objet ``a_1`` ?
#. Modifier le code de la classe ``Fruit`` pour que l'instanciation ``a_1 = Fruit('pommes',masse=1,prix=3.20)`` représente 1 kg de pommes à l'instanciation de l'objet.

Exercice 2
----------

On donne la classe ``Personne`` écrite en langage Python:

.. literalinclude:: ../python/personne.py

#. On instancie un premier objet ``p_1 = Personne('Alice',9,'magie')``. Quelles sont les valeurs des attributs de l'objet ``p_1`` ?
#. Quelle est l'instruction Python qui instancie la variable ``p_2`` représentant la personne nommée Bob, âgée de 7 ans et qui n'a pas de hobby ?
#. L'instruction Python ``p_3 = Personne('Carlo','musique',75)`` renvoie-t-elle une erreur ? Si non, est-elle correcte ? Justifier.

Exercice 3
----------

On considère le tableau de données suivant:

.. csv-table::
   :header: nom, age, jeu, sport, instrument
   :align: center
   :widths: 6,4,8,8,8
   :file: ../csv/identite.csv

On veut représenter ces données par des **objets** construits avec la classe ``Identite``.

#. Quels sont les attributs à définir pour la classe ``Identite`` ?
#. Écrire en Python, la classe ``Identite`` avec son constructeur définissant les attributs de nos objets.
#. Instancier 3 objets avec les variables ``p_1``, ``p_2`` et ``p_3`` représentant les données du tableau.
#. La fonction ``age_moyen`` prend en paramètre une **liste** d'objets et renvoie l'âge moyen des différents objets. Écrire en Python cette fonction et calculer l'âge moyen de nos 3 objets.
#. Ajouter une méthode ``afficher`` qui affiche pour chaque objet les différents attributs et leurs valeurs. Par exemple:

   **Alice**

   - âge:9
   - jeu:cartes
   - sport:course
   - instrument:piano

Exercice 4
----------

Un site de vente en ligne propose des articles de bricolage à la vente. Pour chaque article, celui-ci a:

- une référence sous forme de chaine alpha-numérique;
- une désignation sous forme de chaine de caractères;
- un prix sous forme de nombre

On donne ci-dessous un exemple d'articles que l'on peut trouver sur le site:

.. csv-table::
   :header: ref, désignation, prix (€)
   :align: center
   :widths: 5,15,10
   :file: ../csv/article.csv

#. Écrire la classe Article et son constructeur permettant de créer des objets pour les outils de bricolage.
#. Créer les trois objets du site présents dans le tableau ci-dessus.
#. La méthode ``modifier_prix`` permet de modifier le prix d'un article en y appliquant un pourcentage d'augmentation ou de réduction. Cette méthode prend en argument un pourcentage sous forme de nombre entier à appliquer et renvoie le prix modifié de l'article.

   a. Écrire en Python la méthode ``modifier_prix``.
   b. Appliquer une réduction de 10% sur le premier article et une augmentation de 20% sur le second.

   .. note::

      - Un prix augmenté de t% est un prix multiplié par :math:`1+\frac{t}{100}`. 
      - Un prix réduit de t% est un prix multiplié par :math:`1-\frac{t}{100}`. 

