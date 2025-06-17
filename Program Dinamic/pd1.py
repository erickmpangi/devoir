from bisect import bisect_right
import sys

lines = [line.strip() for line in sys.stdin if line.strip()]

# Si la première ligne ne contient pas trois entiers, on l'ignore
if len(lines[0].split()) != 3:
    lines = lines[1:]

tasks = []
for idx, line in enumerate(lines, start=1):
    parts = line.split()
    if len(parts) == 3:
        s, f, p = map(int, parts)
        tasks.append((s, f, p, idx))

# Trier les tâches par heure de fin
tasks.sort(key=lambda x: x[1])
n = len(tasks)
dp = [0] * n
parent = [-1] * n
ends = [task[1] for task in tasks]

for i in range(n):
    s_i, f_i, p_i, _ = tasks[i]
    j = bisect_right(ends, s_i) - 1
    incl_profit = p_i + (dp[j] if j >= 0 else 0)
    if incl_profit > (dp[i - 1] if i > 0 else 0):
        dp[i] = incl_profit
        parent[i] = j
    else:
        dp[i] = dp[i - 1]
        parent[i] = parent[i - 1]

# Reconstruire la solution
i = n - 1
selected = []
while i >= 0:
    if parent[i] == -1 or dp[i] != dp[i - 1]:
        selected.append(tasks[i][3])
        i = parent[i]
    else:
        i -= 1

selected.sort()
print(dp[-1])
print(" ".join(map(str, selected)))