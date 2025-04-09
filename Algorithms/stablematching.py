def stable_matching(_, proposer, proposer_prefs, receiver_prefs):
    # Initialisation des variables
    free_proposers = list(proposer_prefs.keys())
    engaged = {}
    proposals = {proposer: 0 for proposer in free_proposers}

    # Création d'un dictionnaire inversé pour les préférences des receveurs
    reverse_prefs = {
        receiver: {proposer: rank for rank, proposer in enumerate(prefs)}
        for receiver, prefs in receiver_prefs.items()
    }

    while free_proposers:
        proposer = free_proposers[0]

        # Vérification que le proposant a encore des préférences à proposer
        if proposals[proposer] >= len(proposer_prefs[proposer]):
            raise ValueError(f"Invalid preference list for {proposer}, missing preferences.")

        # Sélection de la receveuse suivante dans la liste des préférences du proposant
        receiver = proposer_prefs[proposer][proposals[proposer]]
        proposals[proposer] += 1

        if receiver not in engaged:
            # Si la receveuse n'est pas engagée, on l'engage avec le proposant
            engaged[receiver] = proposer
            free_proposers.pop(0)
        else:
            # Si la receveuse est déjà engagée, on compare les préférences
            current_partner = engaged[receiver]
            if reverse_prefs[receiver][proposer] < reverse_prefs[receiver][current_partner]:
                # Si le nouveau proposant est préféré, on met à jour l'engagement
                engaged[receiver] = proposer
                free_proposers.pop(0)
                free_proposers.append(current_partner)

    # Tri des résultats selon l'ordre des proposants
    proposers_order = list(proposer_prefs.keys())
    return sorted([(proposer, receiver) for receiver, proposer in engaged.items()], key=lambda pair: proposers_order.index(pair[0]))

# import subprocess
if __name__ == "__main__":
    import sys

    # Lecture de la première ligne (nombre de participants et genre des proposants)
    first_line = sys.stdin.readline().strip().split()
    if len(first_line) != 2:
        raise ValueError("Invalid input format: First line must contain exactly two values (N and 'm' or 'w').")

    n = int(first_line[0])
    proposer = first_line[1]

    # Lecture des préférences des hommes
    men_prefs = {}
    for _ in range(n):
        data = sys.stdin.readline().strip().split()
        if len(data) != n + 1:
            raise ValueError(f"Invalid preferences list for {data[0]}. Expected {n} preferences.")
        men_prefs[data[0]] = data[1:]

    # Lecture des préférences des femmes
    women_prefs = {}
    for _ in range(n):
        data = sys.stdin.readline().strip().split()
        if len(data) != n + 1:
            raise ValueError(f"Invalid preferences list for {data[0]}. Expected {n} preferences.")
        women_prefs[data[0]] = data[1:]

    # Appel de la fonction stable_matching avec les bonnes entrées
    if proposer == 'm':
        result = stable_matching(n, proposer, men_prefs, women_prefs)
    else:
        result = stable_matching(n, proposer, women_prefs, men_prefs)

    # Affichage des résultats
    for proposer, receiver in result:
        print(proposer, receiver)