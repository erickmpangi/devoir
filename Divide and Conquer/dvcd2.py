import sys
import math

lines = sys.stdin.read().strip().split('\n')
i = 0

while i < len(lines):
    n = int(lines[i])
    i += 1
    points = []

    for _ in range(n):
        x, y = map(int, lines[i].split())
        points.append((x, y))
        i += 1

    min_dist = float('inf')

    for j in range(n):
        for k in range(j + 1, n):
            dx = points[j][0] - points[k][0]
            dy = points[j][1] - points[k][1]
            dist = math.hypot(dx, dy)
            if dist < min_dist:
                min_dist = dist

    print(f"{min_dist:.6f}")
