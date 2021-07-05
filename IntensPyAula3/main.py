# Aula 2: Ciência de Dados - Previsão de Vendas
import pandas as pd

# Passo 1: extração dos dados
tabela = pd.read_csv("advertising.csv")
print(tabela)

# Passo 2: Análise exploratória
# bibliotecas para pltar gráficos
import seaborn as sns
import matplotlib.pyplot as plt # nescessário para usar o seaborn

# mapa de calor para exibir as correlações da tabela
sns.heatmap(tabela.corr(), annot=True, cmap="Wistia") # annot exibe valores nos quadrados; cmap muda as cores
plt.show()

sns.pairplot(tabela)
plt.show()

