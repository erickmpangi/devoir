#!/bin/bash

# Définir le chemin du dossier contenant les fichiers txt
dossier="/home/erick-mpangi/Documents/exerices-python/Algorithms/input"  # Chemin complet vers ton dossier 'input'

# Vérifier si le dossier existe
if [ ! -d "$dossier" ]; then
  echo "Le dossier 'input' n'existe pas!"
  exit 1
fi

# Trouver tous les fichiers .txt dans le dossier
fichiers=$(find "$dossier" -type f -name "*.txt")

# Vérifier si des fichiers .txt existent
if [ -z "$fichiers" ]; then
  echo "Aucun fichier .txt trouvé dans le dossier 'input'."
  exit 1
fi

# Passer tous les fichiers trouvés à ton script Python en tant qu'arguments
python3 matchingcomplet.py $fichiers
