# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pyautogui
import time
import pyperclip
import pandas as pd
import openpyxl
from IPython.display import display

# Pause de uma 1s entre os comandos
from Tools.scripts.dutree import display

pyautogui.PAUSE = 2

# Passo 1 - Abre o navegador
# Aperta a tecla do windows
pyautogui.press('win')
# Digita Chrome
pyautogui.write('Chrome')
# Aperta enter
pyautogui.press('enter')
# Acessa o sistema
link = 'https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga'
# Copia o link com pyperclip
pyperclip.copy(link)
# Cola o link
pyautogui.hotkey('ctrl','v')
# Aperta enter
pyautogui.press('enter')

# Passo 2
# captura a posição do cursor para poder usar o click
# rodar esse códiog apenas para pegar a posição
# |  time.sleep(5)
# |  print( pyautogui.position() )

# click duplo na pasta
time.sleep(3)
pyautogui.click(412, 266, clicks = 2)

# Passo 3
time.sleep(3)
pyautogui.rightClick(412, 266) #clica com o botão direito
time.sleep(3)
pyautogui.click(521, 687)

# Passo 4
# importando base de dados
# usar o 'r' semore que for usar algum endereço de local de arquivo
time.sleep(5)
tabela = pd.read_excel(r"C:\Users\tasso\Downloads\Vendas - Dez.xlsx") # sheets=1 por padrão
#display(tabela) # melhor para exibir tabelas
faturamento = tabela["Valor Final"].sum() # somar a coluna Valor Final
quantidade = tabela["Quantidade"].sum() # soma da coluna Quantidade
print(faturamento)
print(quantidade)

# Passo 5
pyautogui.hotkey('ctrl','t') # Abrir uma aba
# Entrar no gmail
link = "mail.google.com"
pyperclip.copy(link)
pyautogui.hotkey('ctrl','v')
pyautogui.press("enter")
time.sleep(7)
# clicar no botão escrever
#print( pyautogui.position() )
pyautogui.click(30, 168)
# digitar para quem vamos enviar
pyautogui.write("tassoluis+diretoria@gmail.com")
pyautogui.press("tab") # escolher o email
pyautogui.press("tab") # passar para o campo de assunto
# para escrever um texto com caracter especial é preciso usar uma variável
assunto = "Relatório de Vendas"
pyperclip.copy(assunto) # colar pra quem vamos enviar
pyautogui.hotkey('ctrl','v')
pyautogui.press("tab") # passar para o campo de escrever o email
# digitar o corpo do email
texto_email = f"""Prezados, bom dia

O faturamento de ontem foi de: R$ {faturamento:,.2f} 
A quantidade de produtos foi de: {quantidade:,}

abs
Tasso Moraes
"""
pyperclip.copy(texto_email)
pyautogui.hotkey('ctrl','v')
# clicar em enviar
pyautogui.press("tab")
pyautogui.press("enter")

