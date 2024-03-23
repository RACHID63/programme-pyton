import PyPDF2
import json

def pdf_to_json(pdf_path):
    # Ouvrir le fichier PDF en mode lecture binaire
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)

        # Initialiser un dictionnaire pour stocker le contenu
        content = {}

        # Lire chaque page du PDF
        for page in range(len(reader.pages)):
            content[f'Page_{page+1}'] = reader.pages[page].extract_text()

        # Convertir le dictionnaire en format JSON
        json_content = json.dumps(content, indent=4)

        # Sauvegarder dans un fichier JSON
        with open('output.json', 'w') as json_file:
            json_file.write(json_content)

# Remplacer 'your_file.pdf' par le chemin de votre fichier PDF
pdf_to_json('bukhari 1-36.pdf')
