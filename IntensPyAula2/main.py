#Analise de Dados

import pandas as pd
import plotly.express as px

# Passo 1: importar a base de dados
tabela = pd.read_csv("telecom_users.csv")

# Passo 2: visualizar a base de dados
print(tabela)

# Passo 3: tratamento dos dados
print(tabela.info()) # informações de cada coluna
# deleta coluna Unnamed: 0
tabela = tabela.drop("Unnamed: 0", axis=1) # axis 0 para linha e 1 para coluna
# transformar strings em números
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce") # coerce transforma o erro em vazio
# excluindo colunas vazias
# how='all' para todos os valores vazios
# how='any' para algum valor vazio
tabela = tabela.dropna(how="all", axis=1)
# excluindo linhas com valores vazios
tabela = tabela.dropna(how="any", axis=0)
print(tabela.info())

# Passo 4: analise inicial (análise exploratória)
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format)) # normalize=True resultado em %

# Passo 5: Características dos clientes que cancelaram
# color separa cada barra de acordo com o Churn
# sempre que se faz um for em uma tabela ele percorre as colunas (tebela.index para linhas)
for coluna in tabela:
    grafico = px.histogram(tabela, x=coluna, color="Churn")
    grafico.show()