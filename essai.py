import requests
from bs4 import BeautifulSoup

# Fetch the content of the webpage
url = "https://sunnah.com/bukhari/1"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extracting texts that follow titles starting with "Narrated"
narrated_texts = []
for tag in soup.find_all(text=True):
    if tag.strip().startswith("Narrated"):
        narrated_texts.append(tag.strip())

# Preparing content for the PDF
pdf_content = "\n\n".join(narrated_texts)
pdf_content[:1000]  # Displaying a portion for review before generating the PDF
