# %%
import requests as req
url = "https://api.opendota.com/api/proMatches"
dados = req.get(url).json()

# %%
