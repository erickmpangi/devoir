from itertools import permutations

# Fonctions de génération pour chaque type polygonal
def polygonal(s, n):
    if s == 3:
        return n * (n + 1) // 2
    elif s == 4:
        return n * n
    elif s == 5:
        return n * (3 * n - 1) // 2
    elif s == 6:
        return n * (2 * n - 1)
    elif s == 7:
        return n * (5 * n - 3) // 2
    elif s == 8:
        return n * (3 * n - 2)

# Générer les nombres polygonaux à 4 chiffres
polygonals = {s: [] for s in range(3, 9)}

for s in range(3, 9):
    n = 1
    while True:
        p = polygonal(s, n)
        if p >= 10000:
            break
        if p >= 1000:
            polygonals[s].append(p)
        n += 1

# Stocker les nombres sous forme de dictionnaires groupés par les deux premiers chiffres
prefix_dict = {s: {} for s in range(3, 9)}
for s in range(3, 9):
    for p in polygonals[s]:
        prefix = p // 100
        prefix_dict[s].setdefault(prefix, []).append(p)

# Fonction récursive pour trouver la chaîne cyclique
def search(chain, used_types):
    if len(chain) == 6:
        # Vérifier la condition cyclique complète
        if chain[-1] % 100 == chain[0] // 100:
            return chain
        return None

    last_two = chain[-1] % 100
    for s in range(3, 9):
        if s in used_types:
            continue
        if last_two in prefix_dict[s]:
            for next_num in prefix_dict[s][last_two]:
                result = search(chain + [next_num], used_types + [s])
                if result:
                    return result
    return None

# Essayer toutes les permutations de types polygonaux
for perm in permutations(range(3, 9)):
    for start in polygonals[perm[0]]:
        result = search([start], [perm[0]])
        if result:
            print("Ensemble trouvé :", result)
            print("Somme :", sum(result))
            exit()
