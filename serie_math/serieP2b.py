import itertools

# Générer tous les nombres polygonaux à 4 chiffres
polygonal = {3: [], 4: [], 5: [], 6: [], 7: [], 8: []}

for n in range(1, 200):
    t = n * (n + 1) // 2
    if 1000 <= t < 10000:
        polygonal[3].append(t)
    s = n * n
    if 1000 <= s < 10000:
        polygonal[4].append(s)
    p = n * (3 * n - 1) // 2
    if 1000 <= p < 10000:
        polygonal[5].append(p)
    h = n * (2 * n - 1)
    if 1000 <= h < 10000:
        polygonal[6].append(h)
    hept = n * (5 * n - 3) // 2
    if 1000 <= hept < 10000:
        polygonal[7].append(hept)
    o = n * (3 * n - 2)
    if 1000 <= o < 10000:
        polygonal[8].append(o)

# Création d'un dictionnaire pour chercher par préfixe
poly_by_type = {}
for t in polygonal:
    poly_by_type[t] = {}
    for num in polygonal[t]:
        prefix = str(num)[:2]
        poly_by_type[t].setdefault(prefix, []).append(num)

found = False

# Tester toutes les permutations des types
for perm in itertools.permutations([3, 4, 5, 6, 7, 8]):
    for a in polygonal[perm[0]]:
        chain = [a]
        used = {perm[0]}
        def search(chain, used):
            if len(chain) == 6:
                if str(chain[-1])[2:] == str(chain[0])[:2]:
                    print("Solution trouvée :", chain)
                    print("Somme :", sum(chain))
                    return True
                return False
            prefix = str(chain[-1])[2:]
            for t in perm:
                if t in used:
                    continue
                for num in poly_by_type[t].get(prefix, []):
                    if search(chain + [num], used | {t}):
                        return True
            return False
        if search(chain, used):
            found = True
            break
    if found:
        break
