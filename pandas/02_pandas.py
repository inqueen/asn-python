# %%

import pandas as pd

# %%
df_dict = {
    "name": [ "Ana", "Lou", "Dani"],
    "age": [30, 35, 44],
    "sexo": [ "F", "F", "F"]
    }

df = pd.DataFrame(df_dict)
df
# %%
df["name"]
# %%
type(df["name"])
# %%
