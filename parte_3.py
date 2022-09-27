# %%
import random # A MAIS COMUM E UTILIZADA
# import random as rd # PODE SER DESSA FORMA TAMBÉM
# from random import randint # ESSA IMPORTA UMA FUNÇÃO ESPECÍFICA
# from random import * # NÃO É COMUM, MAS ACONTECE
# %%

# %%

# METODO DE MONTE CARLO
N = 670
N = 5
album = set([])

count = 0
while len(album) < N:
    pacote = [random.randint(1,N) for i in range(n)]
    album.update(set(pacote))
    count += 1


# %%
random.randint(1,670)
# %%
# PARTE 3 - SAINDO DO BÁSICO
album = list(range(1,671))

album_conjunto = set(album)

album_conjunto

# %%
