from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Chemin vers le GeckoDriver
geckodriver_path = r'C:\Users\rachi\Downloads\geckodriver-v0.33.0-win64\geckodriver.exe'

# Créer une instance du navigateur Firefox avec Service
service = Service(geckodriver_path)
driver = webdriver.Firefox(service=service)

# Maximiser la fenêtre du navigateur
driver.maximize_window()

# Ouvrir une page web
driver.get('https://www.amazon.fr/Philips-Sonicare-HX3675-15-%C3%A9lectrique/dp/B09QRNV48M/?_encoding=UTF8&pd_rd_w=6lwwg&content-id=amzn1.sym.98e67da0-568f-48db-b234-a79a297c6dc1&pf_rd_p=98e67da0-568f-48db-b234-a79a297c6dc1&pf_rd_r=M9M5X81NS9VATJAYWWK5&pd_rd_wg=OvMZS&pd_rd_r=652bcf32-4a87-45d1-a62b-820274198ce2&ref_=pd_gw_deals_m1_t1&th=1')  # Remplacez par l'URL souhaitée

# Attendre que la page se charge
time.sleep(5)

# Trouver les éléments et récupérer leur texte
element = driver.find_element(By.CLASS_NAME, 'a-price-whole')
element_text = element.get_attribute('textContent')
element1 = driver.find_element(By.CLASS_NAME, 'a-size-medium')
element_text1 = element1.get_attribute('textContent')

print("Prix :", element_text)
print("Stock :", element_text1)

# Créer un DataFrame pour stocker les données
data = pd.DataFrame({'Price': [element_text], 'Stock': [element_text1]})

# Sauvegarder le DataFrame dans un fichier Excel
data.to_excel('output.xlsx', index=False)

# Fermer le navigateur
driver.quit()
