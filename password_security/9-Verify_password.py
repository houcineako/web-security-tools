# Les critères incluent une longueur d'au moins 8 caractères et contenant au moins une lettre majuscule, une lettre minuscule, un chiffre et un caractère spécial (!, @, #, $, %, ou &)


import re

def check_pass(password):
    valid_pass = False
    string_check = True
    special_chars = False
    check_for_whitespace = bool(re.search(r"\s", password))
    
    if len(password_to_test) < 8 or password.islower() or password.isupper() or password.isnumeric():
        string_check = False
        
    for i in password:
        if i in ["!", "@", "#", "$", "%", "&", "*"]:
            special_chars = True
    if string_check == True and special_chars == True and check_for_whitespace == False:
        valid_pass = True
        
    return valid_pass
    
if __name__ == '__main__':
    password_to_test = input("Entrez le mot de passe: ")
    result = check_pass(password_to_test)
    print(f"Le mot de passe est valide: {result}")