# %%
name = "Queen Bey"
print(name)
print(len(name))
# %%
print(name[6])
print(name[8])
print(name[len(name) - 1]) # PODE COLOCAR O LEN() EM UMA VAR TAMBÉM
print(name[-2])
print(name[-3])

# %%
print(name[0:3]) # name[start:stop] range = stop - start (3 - 0)
print(name[:3]) # outra forma de de fazer o mesmo processo
print(name[-3:]) # pega as 3 últimas posições até o infinito
print(name[:-3]) # pula as 3 últimas posições até o infinito
# %%
print(name[4:9]) # fatiar ao meio
# %%
print(name[0:-1]) # todos menos o último
# %%
#STEP
print(name[::2]) # passa por todas as letras de 2 em 2
print(name[:3:2]) # passa pelas 3 primeiras letra de 2 em 2 
# IMPORTANTE -> [START:STOP:STEP]
# %%
print(name[::-1]) # reordena de traz pra frente
# %%
