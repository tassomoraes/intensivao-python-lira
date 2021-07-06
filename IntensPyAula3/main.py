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
#plt.show()

sns.pairplot(tabela)
#plt.show()

# Passo 3: Inteligência Artificial
# dividindo dados de traino e dados de teste
from sklearn.model_selection import train_test_split

y = tabela["Vendas"]
x = tabela.drop("Vendas", axis=1)   # todas as colunas menos a conluna 'Vendas'

x_treino, x_teste, y_treino, y_teste = train_test_split(x,y, test_size=0.3, random_state=1)     # 30% da base de dados é para teste; radom_state sempre mesma forma radomica

# já que o objetivo é número usa-se um método de regressão
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

# criando os modelos
modelo_regressaoLinear = LinearRegression()
modelo_arvoreDeDecisao = RandomForestRegressor()
# treinando os modelos
modelo_regressaoLinear.fit(x_treino,y_treino)
modelo_arvoreDeDecisao.fit(x_treino,y_treino)

# Passo 4: Teste da IA e avaliação do melhor modelo
from sklearn import metrics

# criar a previsão do modelo
previsao_regressaoLinear = modelo_regressaoLinear.predict(x_teste)
previsao_arvoreDeDecisao = modelo_arvoreDeDecisao.predict(x_teste)

# comparar com os resultados
print(metrics.r2_score(y_teste,previsao_regressaoLinear))
print(metrics.r2_score(y_teste,previsao_arvoreDeDecisao))

# Visualização Gráfica das Previsões
tabela_aux = pd.DataFrame() # criar tabela vazia
tabela_aux["y_teste"] = y_teste
tabela_aux["Previsoes ArvoreDecisao"] = previsao_arvoreDeDecisao
tabela_aux["Previsoes RegressaoLinear"] = previsao_regressaoLinear

plt.figure(figsize=(15,5))  # almentando o tamanho do gráfico
sns.lineplot(data=tabela_aux)
plt.show()  # observar a próximadade das linhas

sns.barplot(x=x_treino.columns, y=modelo_arvoreDeDecisao.feature_importances_)
plt.show()