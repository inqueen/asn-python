# %%
import pandas as pd
# %%
path = '/Users/danikarasawa/Desktop/asn_python/pandas/data/order_items.csv'

df = pd.read_csv(path)
df.head()
# %%
df.info()
# %%
df.info(memory_usage='deep')
# %%
df.dtypes
# %%
df.describe(include='all') # PARA VER NO DETALHE, SENÃO, APENAS DF.DESCRIBE()
# %%
prices = ['vlPrice', 'vlFreight']

df[prices]

# MAIS COMUM É ASSIM df[['vlPrice', 'vlFreight']]
# %%

# %%
