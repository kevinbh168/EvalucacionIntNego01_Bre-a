import xlrd
import pandas as pd
import numpy as np

read = pd.read_excel("BI_Clientes.xlsx", sheet_name='Hoja1')
data = pd.DataFrame(read)


# Implementando metodo para obtener datos de tendencia central

def get_mode(name_column):
    mode = read[name_column].mode()
    print('--------------' + name_column + '----------------')
    print("La moda de " + name_column + " es: ", mode)


def get_median(name_column):
    median = read[name_column].median()
    print("La mediana de " + name_column + " es: ", median)


def get_average(name_column):
    average = read[name_column].mean()
    print("El promedio de " + name_column + " es: ", average)


get_mode('YearlyIncome')
get_median('YearlyIncome')
get_average('YearlyIncome')

get_mode('TotalChildren')
get_median('TotalChildren')
get_average('TotalChildren')
