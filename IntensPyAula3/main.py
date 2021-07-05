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
# em caso de correlações altas entre as características excluisse um das características
sns.heatmap(tabela.corr(), annot=True, cmap="Wistia") # annot exibe valores nos quadrados; cmap muda as cores
plt.show()

sns.pairplot(tabela)
plt.show()

# Passo 3: Inteligência Artificial
# dividindo dados de traino e dados de teste
from sklearn.model_selection import train_test_split

y = tabela["Vendas"]
x = tabela.drop("Vendas", axis=1)   # todas as colunas menos a conluna 'Vendas'

x_treino, x_teste, y_treino, y_teste = train_test_split(x,y, test_size=0.3, radom_state=1)     # 30% da base de dados é para teste; radom_state sempre mesma forma radomica

# já que o objetivo é número usa-se um método de regressão
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

#criando os modelos
modelo_regressaoLinear = LinearRegression()
modelo_arvoreDeDecisao = RandomForestRegressor()
#treinando os modelos
modelo_regressaoLinear.fit(x_treino,y_treino)
modelo_arvoreDeDecisao.fit(x_treino,y_treino)