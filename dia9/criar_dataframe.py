import pandas as pd
import numpy as np 

data = {'vendas': [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],}
df = pd.DataFrame(data) #criando o dataframe

#operações
media = df['vendas'].mean() #media
mediana = df['vendas'].median() #mediana
desvio_padrao = df['vendas'].std() #desvio padrão
maximo = df['vendas'].max() #maior valor
minimo = df['vendas'].min() #menor valor

#resultados
print("Media: ", media)
print("Mediana: ", mediana)
print("Desvio padrão: ", desvio_padrao)
print("Maior valor: ", maximo)
print("Menor valor: ", minimo)
