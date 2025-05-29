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




except FileNotFoundError:
    print(f"Erro: O arquivo '{caminho_dados}' não foi encontrado.")
