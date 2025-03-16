"""
Pour lister toutes les URL d'un site Web à l'aide de la bibliothèque de requêtes, vous pouvez la combiner avec une
bibliothèque d'analyse comme BeautifulSoup pour extraire les URL du contenu HTML.
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

target_url = "https://www.wikipedia.org/"
output_file = "wiki_urls_urls.txt"

try:
    response = requests.get(target_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all <a> tags with href attribute
    links = soup.find_all('a', href=True)

    # Extract and save the URLs to a text file
    with open(output_file, "w") as file:
        for link in links:
            full_url = urljoin(target_url, link['href'])
            file.write(full_url + '\n')

    print(f"URLs sauvegarder vers '{output_file}'")
except requests.RequestException as e:
    print(f"Error: {e}")
