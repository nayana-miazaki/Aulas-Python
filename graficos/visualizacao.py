import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

caminho_dados = ('ks-projects-201801.csv')

sb.set_theme(style="whitegrid")

plt.rcParams["figure.figsize"] = (12,6)

df = pd.read_csv(caminho_dados)

# metas_concluidas = df.groupby('goal') > 1000
# df = df['state'].isin['successful','failed']
# print(metas_concluidas)

metas_concluidas_state = df.groupby('state')['goal'].agg(['count']).reset_index()
metas_concluidas_state['percentual'] = (metas_concluidas_state['count']/metas_concluidas_state['count'].sum()) * 100
sb.barplot(data=metas_concluidas_state, x='state', y='percentual', palette='viridis', hue='state')
plt.title('Quantidade de projetos por estado', fontsize=16)
plt.xlabel('Estado do projeto', fontsize=12)
plt.ylabel('Quantidade', fontsize=12)
plt.tight_layout()
plt.show()
# print(metas_concluidas_state)



