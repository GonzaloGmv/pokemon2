import pandas as pd

lista = []
dato = pd.read_csv("Pokemon.csv", header= 0, sep= ",")


del([dato['Type 2']])
del([dato['HP']])
del([dato['Sp. Atk']])
del([dato['Sp. Def']])
del([dato['Speed']])
del([dato['Generation']])
del([dato['Legendary']])

for i in range(len(dato['Type 1'])):
    dato['Type 1'][i] = 'air'

for i in range(len(dato['Type 1'])):
    lista.append('punch')

dato.insert(5, "weapon", lista, allow_duplicates=False)

dato.to_csv('nuevo.csv')

print(dato)