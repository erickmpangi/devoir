import sys
from itertools import combinations

def afficher_combinaisons(elements, k):
    # Générer les combinaisons de k éléments parmi la liste donnée
    combinaisons = combinations(elements, k)
    for comb in combinaisons:
        print(" ".join(map(str, comb)))

try:
    # Lire la première ligne (n et k) depuis l'entrée standard
    first_line = sys.stdin.readline().strip().split()
    if len(first_line) != 2:
        raise ValueError("Format invalide : La première ligne doit contenir exactement deux nombres.")

    n = int(first_line[0])
    k = int(first_line[1])

    if n < 0 or n > 1000:
        print("Erreur : n doit être compris entre 0 et 1000.")
        sys.exit(1)
    elif k < 1 or k > n:
        print("Erreur : k doit être compris entre 1 et n.")
        sys.exit(1)

    # Lire la deuxième ligne (éléments) depuis l'entrée standard
    elements = sys.stdin.readline().strip().split()
    if len(elements) != n:
        raise ValueError(f"Erreur : Vous devez entrer exactement {n} éléments sur la deuxième ligne.")

    afficher_combinaisons(elements, k)

except ValueError as e:
    print(f"Erreur : {e}")
