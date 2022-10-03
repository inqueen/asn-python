# %%
import pandas as pd

# %%
my_list = [30, 25, 34, 65, 78]

sum(my_list) / len(my_list)
# %%
my_list = [30, 25, 34, 65, 78]
my_list = pd.Series(my_list)
my_list.mean()
my_list.median()
my_list.describe()
# %%
my_list.index = list('abcde')
# %%
my_list['b']
# %%
my_list[1] # É COMO SE ELE ESTIVESSE USANDO O my_list.iloc[0] PEGA A POSIÇÃO
# %%
my_list.loc['a'] # PEGA O ÍNDICE 
# %%
my_list * 10 # CRIA UMA NOVA LISTA COM OS MESMOS INDICES
# %%
my_list
# %%
