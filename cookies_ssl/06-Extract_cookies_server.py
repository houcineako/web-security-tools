# Extraire les cookies d'une réponse et les utiliser dans une requête ultérieure

# import requests module
import requests
 
# create a session object
s = requests.Session()
 
# # faire une demande - get request
s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
 
# refaire une demande - get request
r = s.get('https://httpbin.org/cookies')
 
# vérifier si le cookie est toujours défini
print(r.text)