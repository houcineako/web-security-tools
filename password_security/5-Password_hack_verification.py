import hashlib
import requests
import argparse

# Création du parser pour lire les arguments en ligne de commande
parser = argparse.ArgumentParser(description='Vérification de la vulnérabilité du mot de passe')

# Ajout de l'argument pour le mot de passe
parser.add_argument('password', type=str, help="Le mot de passe à vérifier")

# Récupération des arguments
args = parser.parse_args()

# Création d'un objet de hachage SHA1
sha1hash = hashlib.sha1()

# Hachage du mot de passe donné
sha1hash.update(args.password.encode('utf-8'))

# Conversion du hachage en format hexadécimal
sha1digest = sha1hash.hexdigest().upper()

# On prend les 5 premiers caractères du hachage
first_5_of_hash = sha1digest[:5]

print("Vérification du piratage de mot de passe... \n")

# Requête à l'API de Have I Been Pwned avec les 5 premiers caractères du hachage
result = requests.get('https://api.pwnedpasswords.com/range/' + first_5_of_hash)

password_found = False

# Si la requête réussit (code 200)
if result.status_code == 200:
    # Diviser la réponse en lignes
    list_of_passwords = result.text.split('\n')

    # Vérification si le suffixe du mot de passe se trouve dans la liste
    for password in list_of_passwords:
        password_hash_suffix, number_of_times = password.split(':')
        number_of_times = number_of_times.strip()

        # Reconstruction du hachage complet
        full_password_hash = first_5_of_hash + password_hash_suffix

        # Si le hachage du mot de passe correspond
        if sha1digest == full_password_hash:
            print(f'Password {args.password} trouvé {number_of_times} fois!')
            password_found = True

# Si le mot de passe n'est pas trouvé
if not password_found:
    print("Le mot de passe n'a pas été trouvé dans la liste des mots de passe piratés!")
