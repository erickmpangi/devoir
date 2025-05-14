from collections import defaultdict
import sys
sys.setrecursionlimit(10000)  # Juste au cas où les récursions sont profondes

def lire_graphe():
    donnees = list(map(int, sys.stdin.read().split()))
    V, E = donnees[0], donnees[1]
    arretes = [(donnees[i], donnees[i + 1]) for i in range(2, len(donnees), 2)]
    return V, arretes

def construire_graphe(V, arretes):
    graphe = defaultdict(list)
    for u, v in arretes:
        graphe[u].append(v)
        graphe[v].append(u)
    return graphe

def dfs(u, parent, graphe, visited, disc, low, timer, articulation, V):
    visited[u] = True
    disc[u] = low[u] = timer[0]
    timer[0] += 1
    enfants = 0

    for v in graphe[u]:
        if v == parent:
            continue
        if not visited[v]:
            enfants += 1
            dfs(v, u, graphe, visited, disc, low, timer, articulation, V)
            low[u] = min(low[u], low[v])

            # Cas 1 : u est racine et a plus d'un enfant
            if parent == -1 and enfants > 1:
                articulation.add(u)
            # Cas 2 : u n'est pas racine et low[v] >= disc[u]
            if parent != -1 and low[v] >= disc[u]:
                articulation.add(u)
        else:
            low[u] = min(low[u], disc[v])

def trouver_points_de_coupure(V, graphe):
    visited = [False] * (V + 1)
    disc = [float('inf')] * (V + 1)
    low = [float('inf')] * (V + 1)
    timer = [0]
    articulation = set()

    for u in range(1, V + 1):
        if not visited[u]:
            dfs(u, -1, graphe, visited, disc, low, timer, articulation, V)

    return sorted(articulation)

def main():
    V, arretes = lire_graphe()
    graphe = construire_graphe(V, arretes)
    points = trouver_points_de_coupure(V, graphe)
    print(" ".join(map(str, points)))

if __name__ == "__main__":
    main()
