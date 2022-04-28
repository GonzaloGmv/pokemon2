import pandas as pd
import estadistica as est

dato = pd.read_csv("nuevo.csv", header= 0, sep= ",")

hp = est.Estadisticas(dato['HP'])
ataque = est.Estadisticas(dato['Attack'])
defensa = est.Estadisticas(dato['Defense'])

hp.analisisCaracteristica()
ataque.analisisCaracteristica()
defensa.analisisCaracteristica()