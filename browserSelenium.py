from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import pyperclip
import time

# Chemin vers le GeckoDriver
geckodriver_path = r'C:\Users\rachi\Downloads\geckodriver-v0.33.0-win64\geckodriver.exe'

# Créer une instance du navigateur Firefox avec Service
service = Service(geckodriver_path)
driver = webdriver.Firefox(service=service)

# Maximiser la fenêtre du navigateur
driver.maximize_window()

# Ouvrir une page web
driver.get('https://sitefacile.net/')  # Remplacez par l'URL souhaitée

# Attendre que la page se charge
time.sleep(5)

# Trouver l'élément par ID et cliquer dessus
# Remplacez 'id-de-l-element' par l'ID de l'élément sur lequel vous voulez cliquer
element = driver.find_element(By.ID, 'btnGalerie')
element_text = element.click()

# Copier le texte dans le presse-papiers
pyperclip.copy(element_text)

# Attendre un peu après le clic
time.sleep(5)

# Fermer le navigateur
driver.quit()
