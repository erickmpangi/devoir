from collections import deque

# Directions (haut, droite, bas, gauche)
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # U, R, D, L

def bfs(maze, R, C, Sr, Sc, Tr, Tc):
    if maze[Sr][Sc] == '#' or maze[Tr][Tc] == '#':
        return "False", 0, ""

    queue = deque([(Sr, Sc, "")])
    visited = [[False] * C for _ in range(R)]
    visited[Sr][Sc] = True

    while queue:
        x, y, path = queue.popleft()
        if (x, y) == (Tr, Tc):
            return "True", len(path), path

        for i, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and maze[nx][ny] == ' ':
                visited[nx][ny] = True
                new_path = path + "URDL"[i]
                queue.append((nx, ny, new_path))

    return "False", 0, ""

def main():
    try:
        parts = input().split()
        if len(parts) != 7:
            print("Erreur : entrée de paramètres incorrecte")
            return
        R, C, Sr, Sc, Tr, Tc, O = map(int, parts)

        maze = []
        for _ in range(R):
            row = input()
            if len(row) != C:
                print("Erreur : ligne de labyrinthe de longueur incorrecte")
                return
            maze.append(row)

        path_exists, length, path = bfs(maze, R, C, Sr, Sc, Tr, Tc)

        print(path_exists)
        print()
        print("Using the same maze and if the O number is 2 the output is:\n")
        print(length if path_exists == "True" else 0)
        print()
        print("If the O number is 3 the output is:\n")
        print(path if path_exists == "True" else "")

    except Exception as e:
        print("Erreur d'exécution :", e)

if __name__ == "__main__":
    main()
