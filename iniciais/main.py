import os
from unittest.mock import inplace

import pandas as pd

#netflix_titles.csv
caminho_dados = ('D:\\PARTICULAR\\AULAS\\netflix_titles.csv')

try: 
    #Tentar carregar p dados do CSV para um DataFrame
    
    df = pd.read_csv(caminho_dados,sep=',',quotechar='"',engine='python',on_bad_lines='skip')
    
    print("Dados carregados com sucesso")
    print("-" * 30)

    #Mostra informações sobre as colunas (Tipos, valores não nulos)

    print ("Informações do DataFrame/Planilha")
    df.info()
    print("-" * 30)

    print("Dimensões (linhas, colunas):", df.shape)
    print("-" * 30)

    print(df.describe())
    print("-" * 30)

    print(df.nunique())
    print("-" * 30)

    print(df.isnull().sum())
    print("-" * 30)

    print(df.drop('director', axis = 1, inplace = False))
    print("-" * 30)

    print(df.dropna(subset = ['director'], inplace = False))
    print("-" * 30)

    print(df.dropna(subset=['director', 'cast', 'country', 'date_added', 'rating','duration'], how = 'any', inplace=False))
    print("-" * 30)

    linhas_completas = df.dropna()
    print(linhas_completas)
    print("-" * 30)

    print(df.isna().any(axis=1).sum())
    print("-" * 30)

    print(df['director'].fillna(0))
    print("-" * 30)


except FileNotFoundError:
    print(f"Erro: O arquivo '{caminho_dados}' não foi encontrado.")





    