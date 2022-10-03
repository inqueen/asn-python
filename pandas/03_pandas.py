# %%
import pandas as pd

# %%
my_list = pd.Series(
    {"name": "Dani", 
    "age": 44}
)
my_list
# %%

url = '/Users/danikarasawa/Desktop/asn_python/pandas/data/order_items.csv'
df = pd.read_csv(url)
df.head()
# %%
df.tail() # METODO
# %%
df.shape # ATRIBUTO
df.columns
df.columns.to_list()
# %%
