# La fonction sha256() du module hashlib de Python est utilisée pour créer un objet de hachage SHA256. 
# Il s'agit d'une méthode constructeur pour l'algorithme de hachage SHA256. La fonction sha256() prend une entrée de type octet et renvoie une valeur hachée

import hashlib

def encrypt_str(text):
    encrypted_text = hashlib.sha256(text).hexdigest()
    print(f"La valeur hachée est: {encrypted_text}")

if __name__ == '__main__':
    text_to_encrypt = str(input("Entrez le texte à hacher: ")).encode('utf-8')
    encrypt_str(text_to_encrypt)