# %%
# %%
import requests

url = "https://api.opendota.com/api/proPlayers"

response = requests.get(url)
data = response.json()
data[0]
# %%
