import sys
from collections import defaultdict

def main():
    # Lecture de toutes les lignes d'entrée
    data = sys.stdin.read().split()
    idx = 0
    V = int(data[idx])
    E = int(data[idx + 1])
    idx += 2
    edges = []
    for _ in range(E):
        u = int(data[idx])
        v = int(data[idx + 1])
        edges.append((u, v))
        idx += 2

    # Construction du graphe
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (V + 1)
    components = []

    # Fonction DFS pour explorer une composante connexe
    def dfs(node, component):
        stack = [node]
        visited[node] = True
        while stack:
            current = stack.pop()
            component.append(current)
            for neighbor in graph[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append(neighbor)

    # Parcours de tous les sommets
    for node in range(1, V + 1):
        if not visited[node]:
            component = []
            dfs(node, component)
            component.sort()
            components.append(component)

    # Affichage des résultats
    print(len(components))
    for component in components:
        print(' '.join(map(str, component)))

if __name__ == "main":
    main()