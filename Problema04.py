import xlrd
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("BI_Clientes.xlsx", sheet_name='Hoja1')
fig1, ax1 = plt.subplots()


def client_for_genre():
    date_group_by = data.groupby('Gender')['Gender'].count()
    date_group_by.plot(kind='barh')
    plt.xlabel('Numero de clientes')
    plt.show()


def early_amount_genre():
    date_group_by = data.groupby('Gender')['YearlyIncome'].sum()
    date_group_by.plot(kind='bar')
    plt.show()


def average_genre():
    date_group_by = data.groupby('Gender')['YearlyIncome'].mean()
    date_group_by.plot(kind='pie')
    print(date_group_by)
    plt.show()


average_genre()
