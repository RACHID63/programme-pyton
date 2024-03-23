import requests
from bs4 import BeautifulSoup
import json

def scrape_to_json(url):
    try:
        # Obtenir le contenu HTML de la page web
        response = requests.get(url)
        response.raise_for_status()  # Ceci vérifie si la requête a réussi

        # Analyse du contenu HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extraction des données
        # Ceci est un exemple, ajustez la sélection selon vos besoins
        data = {}
        for element in soup.find_all('tag'):  # Remplacez 'tag' par le tag HTML pertinent
            key = element.get('attribut')  # Remplacez 'attribut' par l'attribut HTML pertinent
            value = element.text
            data[key] = value

        # Conversion des données en JSON
        json_data = json.dumps(data, indent=4)

        # Sauvegarde du JSON dans un fichier
        with open('data.json', 'w') as file:
            file.write(json_data)

        print("Données enregistrées dans 'data.json'")

    except requests.HTTPError as http_err:
        print(f"Erreur HTTP : {http_err}")
    except Exception as err:
        print(f"Une erreur s'est produite : {err}")

# Utilisation de la fonction
url = "https://sunnah.com/bukhari/4"  # Remplacez par l'URL de votre choix
scrape_to_json(url)
