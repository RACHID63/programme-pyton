import pdfkit
import requests
from bs4 import BeautifulSoup

# Configuration de pdfkit avec wkhtmltopdf
path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

def save_webpage_as_pdf(url, output_filename):
    try:
        # Récupération du contenu de la page web
        response = requests.get(url)
        response.raise_for_status()  # Lève une exception pour les erreurs HTTP

        # Nettoyage du HTML avec BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        cleaned_html = soup.prettify()

        # Conversion du HTML en PDF
        pdfkit.from_string(cleaned_html, output_filename, configuration=config)
        print(f"PDF créé avec succès : {output_filename}")

    except requests.HTTPError as e:
        print(f"Erreur HTTP lors de la récupération de la page web : {e}")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

# Liste des URLs à convertir
urls = [
    'https://sunnah.com/bukhari/37',
 'https://sunnah.com/bukhari/38',
 'https://sunnah.com/bukhari/39',
 'https://sunnah.com/bukhari/40',
 'https://sunnah.com/bukhari/41'
 
]

# Parcours des URLs et création des PDF
for i, url in enumerate(urls):
    output_filename = f'output_{i+1}.pdf'
    save_webpage_as_pdf(url, output_filename)
