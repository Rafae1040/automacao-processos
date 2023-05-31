# Enviar um e-mail para a diretoria com os indicadores de venda

# abrir aba
pyautogui.hotkey("ctrl", "t")

# entrar no link do email - https://mail.google.com/mail/u/0/#inbox
pyperclip.copy("https://mail.google.com/mail/u/0/#inbox")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(5)

# clicar no botão escrever
pyautogui.click(x=240, y=415)

# preencher as informações do e-mail
pyautogui.write("seunome@gmail.com")
pyautogui.press("tab") # selecionar o email

pyautogui.press("tab") # pular para o campo de assunto
pyperclip.copy("Relatório de Vendas")
pyautogui.hotkey("ctrl", "v")

pyautogui.press("tab") # pular para o campo de corpo do email

texto = f"""
Prezados,

Segue relatório de vendas.
Faturamento: R${faturamento:,.2f}
Quantidade de produtos vendidos: {quantidade:,}

Qualquer dúvida estou à disposição.
Att.,
Rafael M de Carvalho
"""

# formatação dos números (moeda, dinheiro)

pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")

# enviar o e-mail
pyautogui.hotkey("ctrl", "enter")