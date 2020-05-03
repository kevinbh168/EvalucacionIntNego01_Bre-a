import pandas as pd
import numpy as np

leer = pd.read_csv('medallero_Panamericanos_Lima2019.csv')
dataOro = pd.DataFrame(leer['Oro'])
mode_oro = dataOro.mode()
mean_oro = dataOro.mean()
median_oro = dataOro.median()
print('La moda de', mode_oro)
print('Promedio de Oro: ', mean_oro)
print('Mediana: ', median_oro)
print('-----------------------------------------------------')
dataPlata = pd.DataFrame(leer['Plata'])
mode_plata = dataPlata.mode()
mean_plata = dataPlata.mean()
median_plata = dataPlata.median()
print('La moda de', mode_plata)
print('Promedio de Oro: ', mean_plata)
print('Mediana', median_plata)