import pandas as pd
import numpy as np 

data = {'nome': ['Ana', 'João', 'Maria', 'Helena', 'Joana', 'Antonio'], 'departamento': ['Tecinfo', 'RH', 'Engenheiro', 'Professor', 'Tecinfo', 'Engenheiro'], 'salario': [1000, 2000, 3000, 4000, 1500,3500]}

df = pd.DataFrame(data) #criando o dataframe

#filtrar os funcionarios de Tecinfo
tecinfo = df[df['departamento'] == 'Tecinfo']
print(tecinfo)

#media dos salarios dos Tecinfo
media_tecinfo = tecinfo['salario'].mean()
print("A média dos salarios dos Tecinfo é: ", media_tecinfo)

#filtrar os funcionarios de RH
rh = df[df['departamento'] == 'RH']
print(rh)

#media dos salarios dos RH
media_rh = rh['salario'].mean()
print("A média dos salarios dos RH é: ", media_rh)

#filtrar os funcionarios de Engenheiro
engenheiro = df[df['departamento'] == 'Engenheiro']
print(engenheiro)

#media dos salarios dos Engenheiro
media_engenheiro = engenheiro['salario'].mean()
print("A média dos salarios dos Engenheiro é: ", media_engenheiro)

#filtrar os funcionarios de Professor
professor = df[df['departamento'] == 'Professor']
print(professor)

#media dos salarios dos Professor
media_professor = professor['salario'].mean()   
print("A média dos salarios dos Professor é: ", media_professor)    