import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

archivo = "WEO_Data.csv"
data = pd.read_csv(archivo, thousands=',', decimal='.')
data.rename(columns={'Country': 'Pais'}, inplace=True)
data.set_index('Pais', inplace=True)



def grafico2():
    top10 = data.sort_values(by="2020", ascending=True, inplace=True)
    top10 = data['2019'].tail(10)
    top10.plot(kind='bar')
    plt.show()






periodo = list(map(str, range(2019, 2020)))
paises = ['United States', 'China', 'Japan', 'Germany', 'France', 'Brazil', 'Peru']
def grafico1():
    peru = data.loc[paises, periodo]
    peru.plot(kind="bar")
    plt.show()

grafico2()






def grafico3():
    top = data['2020']
    top.plot(kind='hist')
    plt.show()
