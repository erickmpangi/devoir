import math

# Ouvrir le fichier
with open("base_exp.txt", "r") as file:
    max_value = 0
    max_line = 0
    line_number = 0

    # Lire ligne par ligne
    for line in file:
        line_number += 1
        base, exponent = map(int, line.strip().split(","))
        value = exponent * math.log(base)

        if value > max_value:
            max_value = value
            max_line = line_number

print("The line with the highest value is :", max_line)
