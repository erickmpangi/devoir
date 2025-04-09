from stable_matching import stable_matching

if __name__ == "__main__":
    print("Enter the number of participants and who proposes (m/w):")
    first_line = input().strip().split()

    if len(first_line) != 2:
        raise ValueError("Invalid input format: First line must contain exactly two values (N and 'm' or 'w').")

    n = int(first_line[0])
    proposer = first_line[1]

    men_prefs = {}
    women_prefs = {}

    for _ in range(n):
        data = input().strip().split()
        if len(data) != n + 1:
            raise ValueError(f"Invalid preferences list. Each list must have {n} preferences.")
        men_prefs[data[0]] = data[1:]

    for _ in range(n):
        data = input().strip().split()
        if len(data) != n + 1:
            raise ValueError(f"Invalid preferences list. Each list must have {n} preferences.")
        women_prefs[data[0]] = data[1:]

    if proposer == 'w':
        result = stable_matching(n, proposer, women_prefs, men_prefs)
    else:
        result = stable_matching(n, proposer, men_prefs, women_prefs)

    print("Stable matching results:")
    for man, woman in result:
        print(man, woman)
