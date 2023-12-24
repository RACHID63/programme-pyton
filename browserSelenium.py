from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import pyperclip
import time

# Chemin vers le GeckoDriver
geckodriver_path = r'C:\Users\rachi\Downloads\geckodriver-v0.33.0-win64\geckodriver.exe'

# Demander à l'utilisateur de saisir le nom de la classe
# cl = input("Entrez le nom de la classe : ")


# Créer une instance du navigateur Firefox avec Service
service = Service(geckodriver_path)
driver = webdriver.Firefox(service=service)

# Maximiser la fenêtre du navigateur
driver.maximize_window()

# Ouvrir une page web
driver.get('https://www.amazon.fr/TP-Link-Surveillance-Tapo-Bidirectionnel-C200/dp/B07XLML2YS/ref=sr_1_1?_encoding=UTF8&m=A2CVHYRTWLQO9T&pf_rd_p=e921cda4-55c2-425e-a138-38d29289e032&pf_rd_r=6ZDK965P7TGSWJG52A3M&pf_rd_s=auto-subnav-flyout-xiste-content-2&pf_rd_t=SubnavFlyout&qid=1703438326&s=warehouse-deals&sr=1-1&th=1')  # Remplacez par l'URL souhaitée

# Attendre que la page se charge
time.sleep(5)

# Trouver l'élément par ID et cliquer dessus
# Remplacez 'id-de-l-element' par l'ID de l'élément sur lequel vous voulez cliquer

element = driver.find_element(By.CLASS_NAME, 'offer-price')
element_text = element.get_attribute('textContent')


print("Texte récupéré :", element_text)

# Copier le texte dans le presse-papiers
pyperclip.copy(element_text)

# Attendre un peu après le clic
time.sleep(5)

# Fermer le navigateur
driver.quit()
