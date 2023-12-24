import webbrowser
import pyautogui
import time

# Remplacez ceci par le chemin de votre exécutable Firefox si nécessaire
firefox_path = "C:/Program Files/Mozilla Firefox/firefox.exe"

# Ouvrir Firefox
webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefox_path))
webbrowser.get('firefox').open_new_tab('http://www.google.com')

# Attendre un moment pour que le navigateur s'ouvre
time.sleep(5)

# Déplacer la souris à la position désirée
pyautogui.moveTo(1802, 165, duration=1)

# Effectuer un clic de souris à cette position
pyautogui.click()

# Attendre un peu pour s'assurer que la page est prête
time.sleep(2)

# Utiliser un raccourci clavier pour sélectionner tout (Ctrl+A)
pyautogui.hotkey('ctrl', 'a')

# Attendre un peu pour s'assurer que tout est sélectionné
time.sleep(1)

# Appuyer sur la touche "delete" pour effacer le contenu sélectionné
pyautogui.press('delete')

# Attendre un moment pour s'assurer que le contenu est effacé
time.sleep(1)

# Écrire le mot "YouTube"
pyautogui.write('youtube')

# Appuyer sur la touche "Enter"
pyautogui.press('enter')
