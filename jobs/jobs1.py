def read_test_case_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        n = int(lines[0].strip())
        start_times = list(map(int, lines[1].strip().split()))
        end_times = list(map(int, lines[2].strip().split()))
    return n, start_times, end_times

def schedule_jobs(n, start_times, end_times):
    # Créer une liste de tuples (index, start, end)
    jobs = [(i+1, start_times[i], end_times[i]) for i in range(n)]
    # Trier les jobs par heure de fin (greedy)
    jobs.sort(key=lambda x: x[2])

    selected_jobs = []
    last_end_time = 0

    for job in jobs:
        idx, start, end = job
        if start >= last_end_time:
            selected_jobs.append(idx)
            last_end_time = end

    return selected_jobs

def main():
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 planificateur.py <fichier1.txt>")
        return

    file_path = sys.argv[1]
    n, start_times, end_times = read_test_case_from_file(file_path)
    selected_jobs = schedule_jobs(n, start_times, end_times)

    print(len(selected_jobs))
    print(' '.join(map(str, selected_jobs)))

if __name__ == "__main__":
    main()

