def stable_matching(_, proposer, men_prefs, women_prefs):
    free_men = list(men_prefs.keys()) if proposer == 'm' else list(women_prefs.keys())
    engaged = {}
    proposals = {man: 0 for man in free_men}

    reverse_prefs = {}
    for woman, prefs in women_prefs.items():
        reverse_prefs[woman] = {man: rank for rank, man in enumerate(prefs)}

    while free_men:
        man = free_men[0]
        woman = men_prefs[man][proposals[man]]
        proposals[man] += 1

        if woman not in engaged:
            engaged[woman] = man
            free_men.pop(0)
        else:
            current_partner = engaged[woman]
            if reverse_prefs[woman][man] < reverse_prefs[woman][current_partner]:
                engaged[woman] = man
                free_men.pop(0)
                free_men.append(current_partner)

    # Let's ensure the output is ordered based on the original proposers' order
    proposers_order = list(men_prefs.keys()) if proposer == 'm' else list(women_prefs.keys())
    return sorted([(man, woman) for woman, man in engaged.items()], key=lambda pair: proposers_order.index(pair[0]))

if __name__ == "__main__":
    try :
        # print("Enter the number of participants and who proposes (m/w):")
        # first_line = input().strip().split()

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
            # data = input().strip().split()
            if len(data) != n + 1:
                raise ValueError(f"Invalid preferences list. Each list must have {n} preferences.")
            women_prefs[data[0]] = data[1:]

        if proposer == 'w':
            result = stable_matching(n, proposer, women_prefs, men_prefs)
        else:
            result = stable_matching(n, proposer, men_prefs, women_prefs)

        # print("Stable matching results:")
        for man, woman in result:
            print(man, woman)