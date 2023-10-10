import os

directory_path = "."  # Chemin vers le répertoire courant
contents = os.listdir(directory_path)

for item in contents:
    print(item)

directory_path = "."  # Chemin vers le répertoire courant
contents = os.listdir(directory_path)

for item in contents:
    item_path = os.path.join(directory_path, item)
    if os.path.isdir(item_path):
        print(f"Dossier : {item}")
    else:
        print(f"Fichier : {item}")