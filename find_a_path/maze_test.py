from collections import deque

# Directions (haut, droite, bas, gauche) avec leurs lettres respectives
directions = [(-1, 0, 'U'), (0, 1, 'R'), (1, 0, 'D'), (0, -1, 'L')]  # (dx, dy, direction)


# Fonction pour effectuer la recherche du chemin le plus court
def bfs(maze, R, C, Sr, Sc, Tr, Tc):
    # Vérification si la source ou la destination sont dans un mur
    if maze[Sr][Sc] == '#' or maze[Tr][Tc] == '#':
        return "Faux", 0, ""  # Si départ ou arrivée sont dans un mur

    # Initialisation de la queue pour BFS avec la source
    queue = deque([(Sr, Sc, "")])  # Queue de BFS (position, chemin parcouru)
    visited = [[False] * C for _ in range(R)]  # Matrice de visites
    visited[Sr][Sc] = True

    while queue:
        x, y, path = queue.popleft()

        # Si nous avons atteint la destination
        if (x, y) == (Tr, Tc):
            return "Vrai", len(path), path  # Retournons Vrai, longueur et le chemin

        # Essayer de se déplacer dans les 4 directions
        for dx, dy, direction in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and maze[nx][ny] == ' ':
                visited[nx][ny] = True
                queue.append((nx, ny, path + direction))

    # Si aucun chemin n'est trouvé
    return "Faux", 0, ""  # Retourne Faux, 0 et un chemin vide si aucun chemin trouvé


# Fonction principale
def main():
    # Entrée des données
    R, C, Sr, Sc, Tr, Tc, O = map(int, input().split())
    maze = [input().strip() for _ in range(R)]

    # Appeler la fonction BFS et obtenir le résultat
    result = bfs(maze, R, C, Sr, Sc, Tr, Tc)

    # Affichage des résultats sous forme d'une seule ligne
    print(f"{result[0]} {result[1]} {result[2]}")


# Appel de la fonction principale
if __name__ == "__main__":
    main()