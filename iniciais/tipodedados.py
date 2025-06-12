import os
from unittest.mock import inplace

import pandas as pd
# import locale
# locale.setlocale(locale.LC_TIME, 'Portuguese_Brazil.1252')

# netflix_titles.csv
caminho_dados = ('D:\\PARTICULAR\\AULAS\\netflix_titles.csv')

try:
    # Tentar carregar p dados do CSV para um DataFrame

    df = pd.read_csv(caminho_dados, sep=',', quotechar='"', engine='python', on_bad_lines='skip')

    # dataadicionado = pd.to_datetime(df['date_added'],format='%d/%m/%y',errors='coerce')
    # print(dataadicionado)

    data = pd.to_datetime('September 25, 2021')
    print(data)

    data = pd.to_datetime('September 25, 2021', format='%B %d, %Y')
    print(data)

    data = pd.to_datetime(df['date_added'], format='%B %d, %Y',errors='coerce')
    print(data)
    print("-" * 30)

    data = pd.to_datetime(df['date_added'], format='%B %d, %Y',errors='coerce')
    data_formatada = data.dt.strftime('%d/%m/%Y')
    print(data_formatada)

    df.info()

except FileNotFoundError:
    print(f"Erro: O arquivo '{caminho_dados}' não foi encontrado.")
