#Program in Python that asks the user to enter a list of names separated by a comma, then displays the list in reverse order:

names = input("Enter a list of names separated by a comma : ")
names_list = names.split(",")
names_list = [name.strip() for name in names_list]
print("Reverse list :", ", ".join(reversed(names_list)))

# Demander à l'utilisateur d'entrer un nombre entier positif
num = int(input("Entrez un nombre entier positif : "))

# Vérifier si le nombre est négatif
if num < 0:
    print("Le factoriel n'existe pas pour les nombres négatifs.")
elif num == 0 or num == 1:
    print(f"Le factoriel de {num} est 1")
else:
    fact = 1
    for i in range(2, num + 1):  # Boucle de 2 à num
        fact *= i
    print(f"Le factoriel de {num} est {fact}")
