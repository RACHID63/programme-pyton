import requests
from bs4 import BeautifulSoup
import json

# URL de la page à extraire
url = "https://sunnah.com/bukhari/"

# Nom du fichier où sauvegarder le résultat
filename = "/mnt/data/hadith_data.json"

# Effectuer une requête GET pour récupérer le contenu de la page
response = requests.get(url)
data = []

# Si la requête est réussie, procéder à l'extraction des données
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Trouver toutes les divs qui contiennent les hadiths narrés
    hadith_narrated = soup.find_all("div", class_="hadith_narrated")
    
    for hadith in hadith_narrated:
        # Pour chaque hadith, trouver la div de détails de texte
        text_details = hadith.find_next_sibling("div", class_="text_details")
        
        # Extraire le texte (ou tout autre élément nécessaire) de ces divs
        data.append({
            "hadith_narrated": hadith.text.strip(),
            "text_details": text_details.text.strip() if text_details else "N/A"
        })

    # Convertir les données extraites en format JSON
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"Data has been successfully saved to {filename}")
else:
    print(f"Failed to retrieve content from {url}, status code: {response.status_code}")
