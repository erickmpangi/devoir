import random
import os  # Importer le module os pour la gestion des fichiers et dossiers

def generate_preferences(num_participants):
    """
    Generates random preferences for men and women.
    Each man and woman ranks all the participants randomly except for themselves.
    """
    men_prefs = {}
    women_prefs = {}

    # Create participants as "m1", "m2", ..., "mn" for men and "w1", "w2", ..., "wn" for women
    men = [f'm{i}' for i in range(1, num_participants + 1)]
    women = [f'w{i}' for i in range(1, num_participants + 1)]

    # Generate men's preferences
    for man in men:
        preferences = random.sample([woman for woman in women], len(women))
        men_prefs[man] = preferences

    # Generate women's preferences
    for woman in women:
        preferences = random.sample([man for man in men], len(men))
        women_prefs[woman] = preferences

    return men, women, men_prefs, women_prefs

def save_preferences_to_txt(num_participants, men, women, men_prefs, women_prefs):
    """
    Saves the generated preferences to a .txt file.
    The file is named "input_<num_participants>.txt" and saved in the 'input' folder.
    """
    # Create the 'input' directory if it doesn't exist
    os.makedirs('input', exist_ok=True)

    # Save the file inside the 'input' directory
    with open(f'input/input_{num_participants}.txt', mode='w') as file:  # Save inside 'input' folder
        # Write the size of the matching
        file.write(f"{num_participants} m\n")

        # Write men's preferences
        for man in men:
            file.write(f"{man} " + " ".join(men_prefs[man]) + "\n")

        # Write women's preferences
        for woman in women:
            file.write(f"{woman} " + " ".join(women_prefs[woman]) + "\n")

if __name__ == "__main__":
    # Ask the user for the number of participants (input integer)
    num_participants = int(input("Enter the number of participants: "))

    # Generate preferences and save them for the given number of participants
    men, women, men_prefs, women_prefs = generate_preferences(num_participants)
    save_preferences_to_txt(num_participants, men, women, men_prefs, women_prefs)
    print(f"Generated dataset for {num_participants} men and women. The file is named 'input/input_{num_participants}.txt'.")
