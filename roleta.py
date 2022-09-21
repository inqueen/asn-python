# %%
roleta = 10
palpite = int(input("Tente adivinhar o número da sorte:"))

if roleta == palpite:
    print("Você acertou!")

elif palpite > roleta:
    print("Você error! Tente um número menor")

else:
    print("Você error! Tente um número maior")
# %%
