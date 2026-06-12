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

    adjacent = np.zeros((sizeM, sizeM))

    for ligne,colonne in arretes:
        adjacent[ligne-1, colonne-1] = 1

    return adjacent
