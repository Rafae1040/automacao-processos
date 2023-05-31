import pyautogui
import pyperclip
import time

pyautogui.PAUSE = 1

# pyautogui.click -> clicar
# pyautogui.press -> apertar 1 tecla
# pyautogui.hotkey -> conjunto de teclas
# pyautogui.write -> escreve um texto

# Entrar no sistema da empresa (no nosso caso é o link do drive)
pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://drive.google.com/drive/folders")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

time.sleep(5)

# Navegar no sistema e encontrar a base de vendas (entrar na pasta exportar)
pyautogui.click(x=398, y=334, clicks=2)
time.sleep(2)

# Fazer o download da base de vendas
pyautogui.click(x=371, y=404) # clicar no arquivo
pyautogui.click(x=496, y=334) # clicar nos 3 pontinhos
pyautogui.click(x=563, y=503) # clicar no fazer download
time.sleep(5) # esperar o download acabar