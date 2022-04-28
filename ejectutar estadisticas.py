import pandas as pd
import estadistica as est

dato = pd.read_csv("nuevo.csv", header= 0, sep= ",")

hp = est.Estadisticas(dato['HP'])
ataque = est.Estadisticas(dato['Attack'])
defensa = est.Estadisticas(dato['Defense'])

print('Estas son las estadísticas de health points de todos los pokemons')
hp.analisisCaracteristica()
print('Estas son las estadísticas de ataque de todos los pokemons')
ataque.analisisCaracteristica()
print('Estas son las estadísticas de defensa de todos los pokemons')
defensa.analisisCaracteristica()