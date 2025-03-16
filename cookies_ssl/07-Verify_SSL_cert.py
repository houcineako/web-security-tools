import requests   

# Réalisation d'une requête GET avec vérification du certificat SSL
response = requests.get('https://google.com/', verify=True)

print("Response code:", response.status_code)  # Affiche le code de réponse

print("\n----------------------------------\n")
