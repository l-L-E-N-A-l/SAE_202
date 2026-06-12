import numpy as np

def create_matrix_adjacent(arretes: list, sizeM: int) -> np.matrix:
    """
    Créer la matrice d'adjacence à partir d'une liste d'arrêtes.

    Entrée :
    | list : arretes -> La liste des arrêtes de la matrice
    | int  : sizeM   -> La taille de la matrice

    Sortie : 
    | np.matrix : adjacent -> La matrice d'adjacence
    """

    adjacent = [[0 for i in range(sizeM)] for i in range(sizeM)]

    for ligne,colonne in arretes:
        adjacent[ligne-1][colonne-1] = 1

    return adjacent

def afficher_matrice(matrice):
    print('[')
    for i in range(len(matrice)):
        print(matrice[i], ',')
    print(']')

aretes = [(10, 1), (10, 2),(10, 3), (10, 4), (10, 8), (10, 9), (10, 11), 
          (11, 1), (11, 2), (11, 3), (11, 4), (11, 8), (11, 9), (11, 10), 
          (11, 12), (12, 1), (12, 2), (12, 3), (12, 4), (12, 8), (12, 9),
          (12, 11), (12, 13), (13, 1), (13, 2), (13, 3), (13, 4), (13, 8),
          (13, 9), (13, 12), (13, 14), (14, 1), (14, 2), (14, 3), (14, 4),
          (14, 8), (14, 9), (14, 13), (1, 5), (2, 5), (3, 6), (4, 6), (8, 7),
          (9, 7), (5, 6), (5, 7), (6, 5), (6, 7), (7, 5), (7, 6)]

afficher_matrice(create_matrix_adjacent(aretes, 14))