import requests
from bs4 import BeautifulSoup

target_url = "https://www.wikipedia.org/"

try:
    response = requests.get(target_url)  
    if response.status_code == 200:  
        extract_html_text = BeautifulSoup(response.text, "html.parser") 
        get_content = extract_html_text.find("p")  
        
      
        if get_content:
            print(f"Informations recueillies auprès de {target_url}:\n{get_content.text}")
        else:
            print(f"Aucun contenu trouvé dans les balises <p> sur la page {target_url}")
    else:
        print(f"Impossible de récupérer les informations. Code d'état: {response.status_code}")
except requests.RequestException as e:
    print(f"Error: {e}") 
