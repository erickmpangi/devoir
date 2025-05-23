import sys

lines = sys.stdin.read().strip().split('\n')
i = 0

while i < len(lines):
    if not lines[i]:
        i += 1
        continue

    n = int(lines[i])
    i += 1
    t_list = list(map(int, lines[i].split()))
    i += 1
    d_list = list(map(int, lines[i].split()))
    i += 1

    # Création des jobs avec leurs indices
    jobs = []
    for j in range(n):
        jobs.append((d_list[j], j + 1, t_list[j]))  # (date limite, index original, temps)

    # Tri des jobs par date limite croissante
    jobs.sort()

    current_time = 0
    max_retard = 0
    ordre_jobs = []

    for d, index, t in jobs:
        current_time += t
        retard = max(0, current_time - d)
        max_retard = max(max_retard, retard)
        ordre_jobs.append(index)

    print(max_retard)
    print(" ".join(map(str, ordre_jobs)))