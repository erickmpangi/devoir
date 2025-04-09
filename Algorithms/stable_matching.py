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