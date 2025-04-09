import random
import csv


def generate_preferences(num_participants):
    """
    Generates random preferences for men and women.
    Each man and woman ranks all the participants randomly except for themselves.
    """
    men_prefs = {}
    women_prefs = {}

    participants = [f'Person_{i}' for i in range(1, num_participants + 1)]

    # Generate men's preferences
    for man in participants:
        preferences = random.sample([woman for woman in participants if woman != man], len(participants) - 1)
        men_prefs[man] = preferences

    # Generate women's preferences
    for woman in participants:
        preferences = random.sample([man for man in participants if man != woman], len(participants) - 1)
        women_prefs[woman] = preferences

    return men_prefs, women_prefs


def save_preferences_to_csv(num_participants, men_prefs, women_prefs):
    """
    Saves the generated preferences to a CSV file.
    """
    with open(f'preferences_{num_participants}_m.csv', mode='w', newline='') as file:
        writer = csv.writer(file)

        # Writing header for the CSV file
        writer.writerow(['Proposer', 'Receiver Preferences'])

        # Writing men's preferences
        for man, preferences in men_prefs.items():
            writer.writerow([man] + preferences)

        # Writing women's preferences
        for woman, preferences in women_prefs.items():
            writer.writerow([woman] + preferences)


if __name__ == "__main__":
    # Generate preferences and save them for each number of participants from 1 to 1000
    for m in range(1, 1001):  # From 1 to 1000
        men_prefs, women_prefs = generate_preferences(m)
        save_preferences_to_csv(m, men_prefs, women_prefs)
        print(f"Generated dataset for {m} men and women.")
