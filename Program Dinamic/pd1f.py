import sys

lines = sys.stdin.read().splitlines()
tests = []
i = 0
while i < len(lines):
    if not lines[i].strip().isdigit():
        i += 1
        continue
    n = int(lines[i])
    i += 1
    jobs = []
    for _ in range(n):
        if i >= len(lines):
            break
        parts = lines[i].strip().split()
        if len(parts) != 3:
            i += 1
            continue
        st, ft, profit = map(int, parts)
        jobs.append((st, ft, profit, len(jobs) + 1))  # index de tâche (1-based)
        i += 1
    if jobs:
        tests.append(jobs)

for jobs in tests:
    jobs.sort(key=lambda x: x[1])
    n = len(jobs)
    dp = [0] * n
    parent = [-1] * n
    dp[0] = jobs[0][2]

    for i in range(1, n):
        incl_prof = jobs[i][2]
        # Binary search inline
        lo, hi = 0, i - 1
        l = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if jobs[mid][1] <= jobs[i][0]:
                if mid + 1 < i and jobs[mid + 1][1] <= jobs[i][0]:
                    lo = mid + 1
                else:
                    l = mid
                    break
            else:
                hi = mid - 1
        if l != -1:
            incl_prof += dp[l]
        if incl_prof > dp[i - 1]:
            dp[i] = incl_prof
            parent[i] = l
        else:
            dp[i] = dp[i - 1]
            parent[i] = parent[i - 1]

    # Reconstruction du chemin
    selected = []
    i = n - 1
    while i >= 0:
        # Binary search inline à nouveau
        lo, hi = 0, i - 1
        l = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if jobs[mid][1] <= jobs[i][0]:
                if mid + 1 < i and jobs[mid + 1][1] <= jobs[i][0]:
                    lo = mid + 1
                else:
                    l = mid
                    break
            else:
                hi = mid - 1
        if jobs[i][2] + (dp[l] if l != -1 else 0) > (dp[i - 1] if i >= 1 else 0):
            selected.append(jobs[i][3])
            i = l
        else:
            i -= 1

    print(dp[n - 1])
    print(' '.join(map(str, sorted(selected))))