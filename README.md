# Taquin

Le taquin est modélisé par la classe `Jeu_Taquin` ayant pour attributs son état, son profondeur, son parent et son dimension.
On définit les fonctions suivantes:
- `sous_noeuds` qui permet de développer les chemins possibles à partir de l’état courant. 
- `permuter` est une fonction de transition.
- `afficher` va afficher l’état du noeud passé en paramètre.
- `afficher_performance` va afficher le nombre de noeuds visités ainsi que le chemin de la solution optimale.

Les dimensions du taquin ainsi que l’état initial sont donnés en entré.
L’état final est une liste des nombres allant de 0 à n (dimension du taquin) triés par ordre croissant.
