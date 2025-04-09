import matplotlib.pyplot as plt
import numpy as np
import csv

# Fonction pour lire les données du fichier CSV
def read_execution_times_from_csv(file_name):
    N_values = []
    execution_times = []
    
    # Lire le fichier CSV
    with open(file_name, mode='r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Ignorer l'en-tête
        
        # Lire chaque ligne et extraire les valeurs
        for row in reader:
            file_number = int(row[0])  # Numéro du fichier
            num_preferences = int(row[1])  # Nombre de préférences
            start_time = row[2]  # Heure de début (non utilisée ici)
            execution_time = float(row[3])  # Temps d'exécution
            
            N_values.append(num_preferences)
            execution_times.append(execution_time)

    return N_values, execution_times

# Lire les données depuis le fichier CSV
N_values, execution_times = read_execution_times_from_csv('execution_times.csv')

# Créer le graphique
plt.figure(figsize=(8, 6))

# Tracé sur une échelle linéaire
plt.subplot(121)  # 1 ligne, 2 colonnes, premier graphique
plt.plot(N_values, execution_times, marker='o', color='red', label='Execution Time')
plt.title('Execution Time vs. N (Linear Scale)')
plt.xlabel('Number of Preferences (N)')
plt.ylabel('Execution Time (seconds)')
plt.grid(True)

# Tracé sur une échelle logarithmique
plt.subplot(122)  # 1 ligne, 2 colonnes, second graphique
plt.plot(N_values, execution_times, marker='o', color='blue', label='Execution Time')
plt.yscale('log')
plt.xscale('log')
plt.title('Execution Time vs. N (Logarithmic Scale)')
plt.xlabel('Number of Preferences (N)')
plt.ylabel('Execution Time (seconds)')
plt.grid(True)

# Sauvegarder le graphique sous forme de fichier PNG
plt.tight_layout()
plt.savefig('execution_time_graph.png')

# Optionnellement, afficher le graphique
# plt.show()
