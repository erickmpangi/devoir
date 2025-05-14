from collections import defaultdict, deque

def est_biparti(graphe, V):
    couleurs = [-1] * (V + 1)  # -1 signifie non colorié
    for debut in range(1, V + 1):
        if couleurs[debut] == -1:
            file = deque([debut])
            couleurs[debut] = 0  # Commencer avec la couleur 0

            while file:
                sommet = file.popleft()
                for voisin in graphe[sommet]:
                    if couleurs[voisin] == -1:
                        couleurs[voisin] = 1 - couleurs[sommet]  # Alterner les couleurs
                        file.append(voisin)
                    elif couleurs[voisin] == couleurs[sommet]:
                        return None  # Conflit de couleurs → pas biparti

    # Si biparti, séparer les ensembles U et V selon la couleur
    U = [i for i in range(1, V + 1) if couleurs[i] == 0]
    V = [i for i in range(1, V + 1) if couleurs[i] == 1]
    return sorted(U), sorted(V)

def lire_entree():
    import sys
    data = list(map(int, sys.stdin.read().split()))
    V, E = data[0], data[1]
    arretes = data[2:]
    graphe = defaultdict(list)

    for i in range(0, len(arretes), 2):
        u, v = arretes[i], arretes[i + 1]
        graphe[u].append(v)
        graphe[v].append(u)

    return V, graphe

def main():
    V, graphe = lire_entree()
    resultat = est_biparti(graphe, V)
    if resultat is None:
        print("EMPTY")
    else:
        U, V = resultat
        print(" ".join(map(str, U)))
        print(" ".join(map(str, V)))

if __name__ == "__main__":
    main()
