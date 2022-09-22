# %%
# EXERCICIO 2.2

name = input("Digite seu nome:")
age = int(input("Digite sua idade:"))

if(age < 18):
    print(f"{name}, você não pode dirigir nem beber")

elif(age <= 65):
    print(f"{name}, bebida liberada! Só não vale dirigir!”")

else: 
    print(f"{name}, beba com muita moderação! E não misture com medicamentos")
# %%

# EXERCICIO 2.3

number = int(input("Digite um número"))

if(number % 2 == 0):
    print(f"{number} é um número par")

else: 
    print(f"{number} é um número ímpar")
# %%
