def matching_list(men_prefs, women_prefs):
    # Initialisation
    free_men = list(men_prefs.keys())
    matches = {}  # Dictionnaire pour stocker les couples

    while free_men:
        man = free_men.pop(0)  # Prendre le premier homme libre
        woman = men_prefs[man].pop(0)  # Prendre la femme préférée de l'homme

        if woman not in matches:
            # Si la femme est libre, on les associe
            matches[woman] = man
        else:
            # Sinon, on compare les préférences de la femme
            current_man = matches[woman]
            if women_prefs[woman].index(man) < women_prefs[woman].index(current_man):
                # La femme préfère le nouvel homme
                matches[woman] = man
                free_men.append(current_man)  # L'ancien homme redevient libre
            else:
                # La femme garde son partenaire actuel
                free_men.append(man)  # Le nouvel homme redevient libre

    # Inverser le dictionnaire pour avoir homme -> femme
    return {v: k for k, v in matches.items()}

# Exemple d'utilisation
men_prefs = {
    "Alice": ["Diana", "Eve", "Fiona"],
    "Bob": ["Eve", "Diana", "Fiona"],
    "Charlie": ["Diana", "Eve", "Fiona"]
}

women_prefs = {
    "Diana": ["Alice", "Bob", "Charlie"],
    "Eve": ["Alice","Bob", "Charlie"],
    "Fiona": ["Alice", "Bob", "Charlie"]
}

matching = matching_list(men_prefs, women_prefs)
for man, woman in matching.items():
    print(f"{man} is matching with {woman}")