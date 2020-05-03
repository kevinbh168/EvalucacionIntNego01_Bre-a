import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

archivo = "WEO_Data.csv"
data = pd.read_csv(archivo, thousands=',', decimal='.')
data.rename(columns={'Country': 'Pais'}, inplace=True)
data.set_index('Pais', inplace=True)

periodo = list(map(str, range(2000, 2024)))


def grafico1():
    peru = data.loc[['China', 'United States','Japan'], periodo]
    peru.plot(kind="line")
    plt.show()


def grafico2():
    top10 = data.sort_values(by="2020", ascending=True, inplace=True)
    top10 = data['2020'].tail(10)
    top10.plot(kind='barh')
    plt.show()


def grafico2():
    top10 = data.sort_values(by="2020", ascending=True, inplace=True)
    top10 = data['2020'].tail(10)
    top10.plot(kind='barh')
    plt.show()


def grafico3():
    top = data['2020']
    top.plot(kind='hist')
    plt.show()
