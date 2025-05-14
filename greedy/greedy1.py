import sys

# Read from standard input
lines = sys.stdin.read().splitlines()
n = int(lines[0])
start_times = list(map(int, lines[1].split()))
end_times = list(map(int, lines[2].split()))

# Build the list of jobs with (end_time, start_time, index)
jobs = [(end_times[i], start_times[i], i + 1) for i in range(n)]

# Sort by end time (primary criterion)
jobs.sort()

# Select non-overlapping intervals
selected = []
current_end = -1

for end, start, index in jobs:
    if start >= current_end:
        selected.append(index)
        current_end = end

# Output the result
print(len(selected))
print(" ".join(map(str, sorted(selected))))

