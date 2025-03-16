"""
Un fichier robots.txt indique les liens auxquels on a un droit d'accès sur le site.
Cela sert principalement à éviter de surcharger le site de requêtes

Ce code récupère le fichier «robots.txt» sur le site Web de Wikipédia et l'enregistre localement sous le nom «wiki-robots.txt».
Il illustre un cas d'utilisation courant de la bibliothèque de requêtes pour télécharger un fichier à partir du Web.
"""

import requests

file_url = "https://www.wikipedia.org/robots.txt"

try:
    response = requests.get(file_url)
    with open("wiki-robots.txt", 'wb') as file:
        file.write(response.content)
    print("Fichier téléchargé avec succès.")
except requests.RequestException as e:
    print(f"Erreur: {e}")
