import os
from unittest.mock import inplace

import pandas as pd

# netflix_titles.csv
caminho_dados = ('D:\\PARTICULAR\\AULAS\\netflix_titles.csv')

try:
    # Tentar carregar p dados do CSV para um DataFrame

    df = pd.read_csv(caminho_dados, sep=',', quotechar='"', engine='python', on_bad_lines='skip')

    # Mostra informações sobre as colunas (Tipos, valores não nulos)

    coluna_x = (df['director'])
    print(coluna_x.head())

    coluna_x = df[['director', 'cast', 'country', 'date_added', 'rating','duration']]
    print(coluna_x.head())

    dfcombo = df[(df['rating'] == 'PG-13') & (df['director'] == 'Kirsten Johnson')]
    print(dfcombo)

    dfcombo = df[(df['rating'] == 'PG-13') | (df['director'] == 'Kirsten Johnson')]
    print(dfcombo)


except FileNotFoundError:
    print(f"Erro: O arquivo '{caminho_dados}' não foi encontrado.")

