import pyautogui
import time

try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
        time.sleep(0.1)  # Pause de 0.1 secondes pour ne pas surcharger le processeur
except KeyboardInterrupt:
    print('\nTerminé.')  # Affiché lorsque vous interrompez le programme
