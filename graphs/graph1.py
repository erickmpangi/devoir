from collections import defaultdict
import sys

def lire_graphe():
    # Lire toutes les données d'entrée
    donnees = list(map(int, sys.stdin.read().split()))
    V, E = donnees[0], donnees[1]
    arretes = [(donnees[i], donnees[i + 1]) for i in range(2, len(donnees), 2)]
    return V, E, arretes

def construire_graphe(V, arretes):
    graphe = defaultdict(list)
    for u, v in arretes:
        graphe[u].append(v)
        graphe[v].append(u)  # Non orienté
    return graphe

def dfs(sommet, graphe, visites, composante):
    visites[sommet] = True
    composante.append(sommet)
    for voisin in graphe[sommet]:
        if not visites[voisin]:
            dfs(voisin, graphe, visites, composante)

def trouver_composantes_connexes(V, graphe):
    visites = [False] * (V + 1)
    composantes = []

    for sommet in range(1, V + 1):
        if not visites[sommet]:
            composante = []
            dfs(sommet, graphe, visites, composante)
            composantes.append(sorted(composante))

    return composantes

def main():
    V, E, arretes = lire_graphe()
    graphe = construire_graphe(V, arretes)
    composantes = trouver_composantes_connexes(V, graphe)

    print(len(composantes))
    for composante in composantes:
        print(" ".join(map(str, composante)))

if __name__ == "__main__":
    main()
