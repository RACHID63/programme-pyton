import os
import requests
import json

# Remplacez 'YOUR_API_KEY' par votre clé API Hugging Face
huggingface_api_key = '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'

# Définissez le paragraphe que vous souhaitez convertir en images
paragraph = "La chaleur accablante du marché noir de Syrus City étreignait Léa comme un étau. Ses yeux noisette observaient nerveusement la foule hétéroclite qui s'agitait autour d'elle, tandis que ses doigts serraient convulsivement le petit paquet enveloppé de tissu qu'elle venait d'acquérir au-près d'un receleur louche. Son cœur battait la chamade, rythmé par l'urgence de sa mission."

# Divisez le paragraphe en phrases
sentences = paragraph.split('. ')

# Définissez l'URL de base de l'API Hugging Face
base_url = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-v1"

# Définissez les en-têtes de requête, y compris votre clé API Hugging Face
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {huggingface_api_key}",
}

# Générez des images pour chaque phrase
for i, sentence in enumerate(sentences):
    # Définissez les paramètres de requête pour l'API "Stable Diffusion"
    request_data = {
        "inputs": sentence,
    }

    # Effectuez une requête POST à l'API Hugging Face
    response = requests.post(base_url, headers=headers, json=request_data)

    if response.status_code == 200:
        image_url = response.json()["data"][0]["image"]

        # Téléchargez l'image générée
        image_response = requests.get(image_url)

        # Enregistrez l'image sur le disque
        with open(f"image_{i}.png", "wb") as file:
            file.write(image_response.content)

        print(f"Image generated and saved as image_{i}.png")
    else:
        print(f"Error: {response.status_code} - {response.text}")