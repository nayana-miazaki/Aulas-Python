import os
from unittest.mock import inplace

import pandas as pd

# netflix_titles.csv
caminho_dados = ('D:\\PARTICULAR\\AULAS\\netflix_titles.csv')

try:
    # Tentar carregar p dados do CSV para um DataFrame

    df = pd.read_csv(caminho_dados, sep=',', quotechar='"', engine='python', on_bad_lines='skip')

    print("Dados carregados com sucesso")
    print("-" * 30)

    duplicatas = df.duplicated()
    print(duplicatas)
    print(duplicatas.sum())
    print("-" * 30)

    duplicadas = df.drop_duplicates(inplace=True)
    print(duplicadas)
    print("-" * 30)

    duplicatas = df.duplicated()
    print(duplicatas)
    print(duplicatas.sum())
    print("-" * 30)

    #Convertendo para letras maiusculas
    df['MOVIE'] = df['type'].str.upper()
    print(df['MOVIE'])
    print("-" * 30)


    def categoria(row):
        if row['type'] == 'MOVIE':
            return 'MOVIE'
        if row['type'] == 'TV SHOW':
            return 'TV SHOW'
        return row['type']

    print(df)

except FileNotFoundError:
    print(f"Erro: O arquivo '{caminho_dados}' não foi encontrado.")
