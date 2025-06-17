import sys

# Lire toutes les lignes de l'entrée
lines = [line.strip() for line in sys.stdin if line.strip()]
i = 0

while i < len(lines):
    # Lire nombre d'objets et capacité du sac
    it, w = map(int, lines[i].split())
    i += 1

    # Lire les valeurs et poids
    values = []
    weights = []
    for _ in range(it):
        v, wi = map(int, lines[i].split())
        values.append(v)
        weights.append(wi)
        i += 1

    # Création de la table DP (it+1 x w+1)
    dp = [[0] * (w + 1) for _ in range(it + 1)]

    for j in range(1, it + 1):
        for k in range(w + 1):
            if weights[j - 1] <= k:
                dp[j][k] = max(dp[j - 1][k], dp[j - 1][k - weights[j - 1]] + values[j - 1])
            else:
                dp[j][k] = dp[j - 1][k]

    # Afficher le profit maximal
    print(dp[it][w])

    # Reconstituer les objets sélectionnés
    res = []
    k = w
    for j in range(it, 0, -1):
        if dp[j][k] != dp[j - 1][k]:
            res.append(j)  # index à partir de 1
            k -= weights[j - 1]

    res.sort()
    print(" ".join(map(str, res)))