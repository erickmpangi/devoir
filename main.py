import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+']

print("WELCOME TO THE PASSWORD GENERATOR")

number_letters = int(input("How many letters would you like in your password ? :\n"))
number_symbols = int(input("How many symbols would you want in your password ? : \n"))
number_numbers = int(input("How many numbers would you want in your password ? : \n"))

letter = 0
number = 0
symbol = 0
password_list = []
password = ""
for l in range(0, number_letters):
    password_list.append(random.choice(letters))
    # print(letters[letter])
for s in range(0,number_symbols):
    password_list += random.choice(symbols)
    # print(symbols[symbol])
for n in range(0,number_numbers):
    password_list += random.choice(numbers)
    # print(password_list)
random.shuffle(password_list)
for p in password_list:
    password += p
print(f'Your password is {password}')

# programme qui genere 100 ficier txt
import random


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
    """
    with open(f'preferences_{num_participants}.txt', mode='w') as file:
        # Write the size of the matching
        file.write(f"{num_participants} m\n")

        # Write men's preferences
        for man in men:
            file.write(f"{man} " + " ".join(men_prefs[man]) + "\n")

        # Write women's preferences
        for woman in women:
            file.write(f"{woman} " + " ".join(women_prefs[woman]) + "\n")


if __name__ == "__main__":
    # Generate preferences and save them for each number of participants from 1 to 1000
    for m in range(1, 1001):  # From 1 to 1000
        men, women, men_prefs, women_prefs = generate_preferences(m)
        save_preferences_to_txt(m, men, women, men_prefs, women_prefs)
        print(f"Generated dataset for {m} men and women.")

