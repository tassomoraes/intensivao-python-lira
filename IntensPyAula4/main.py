# Aula 4: Automação Web e Busca de Informações com Python

# selenio permite automatizar o navegador
# permite trabalhar em paralelo a automação
# para usa-lo é preciso primeiro importar
from selenium import webdriver
from selenium.webdriver.common.keys import Keys # permite apertar alguma tecla no navegador

# setup para rodar o chrome em 2º plano
# recomenda-se rodar primeiro em 1º plano
# from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# chrome_options.headless = True
# nav = webdriver.Chrome(options=chrome_options)

# Passo 1: pegar cotações dólar, euro e ouro
# abrir navegador
navegador = webdriver.Chrome()
# entrar em um endereço
navegador.get("https://www.google.com/")
# Dólar
# escrever no campo de busca no google
navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação dólar")
# preciona ENTER
navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
# pegar um informação no navegador
cotacao_dolar = navegador.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")
print(cotacao_dolar)

# Euro
navegador.get("https://www.google.com/")
navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação euro")
navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacao_euro = navegador.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")
print(cotacao_euro)

# Ouro
navegador.get("https://dolarhoje.com/ouro-hoje")
cotacao_ouro = navegador.find_element_by_xpath('//*[@id="nacional"]').get_attribute("value")
cotacao_ouro = cotacao_ouro.replace(',','.')
print(cotacao_ouro)

# fechar navegador
navegador.quit()

# Passo 2: Importar a lista de produtos
import pandas as pd
import openpyxl

tabela = pd.read_excel("Produtos.xlsx")
print(tabela)

# Passo 3: recalcular o preço dos produtos
# atualizar a cotação
tabela.loc[tabela["Moeda"]=="Dólar", "Cotação"] = float(cotacao_dolar)
tabela.loc[tabela["Moeda"]=="Euro", "Cotação"] = float(cotacao_euro)
tabela.loc[tabela["Moeda"]=="Ouro", "Cotação"] = float(cotacao_ouro)
# atualizar preço base reais
tabela["Preço Base Reais"] = tabela["Preço Base Original"]*tabela["Cotação"]
# atualizar preço final
tabela["Preçi Final"] = tabela["Preço Base Reais"]*tabela["Margem"]
print(tabela)

# Passo 4: salvar os novos preços dos produtos
