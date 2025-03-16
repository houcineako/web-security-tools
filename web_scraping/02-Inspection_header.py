"""
Ce code Python exécute une requête HTTP GET vers l'URL cible spécifiée (page d'accueil de Wikipédia).
L'objectif principal est de récupérer et d'imprimer l'analyse des en-têtes HTTP de la réponse.
"""


import requests

target_url = "https://www.wikipedia.org/"

try:
    response = requests.get(target_url)
    headers = response.headers
    print(f"HTTP Headers de {target_url}:\n{headers}")
except requests.RequestException as e:
    print(f"Erreur: {e}")