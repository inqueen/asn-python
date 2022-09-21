# %%
# EXERCICIO 1
from re import A


name = input("Digite seu nome:")
print("Olá,", name, "! Seja bem-vinda(o)!", sep="")
# %%
# EXERCICIO 2
name = input("Digite seu nome:")
age = input("Digite a sua idade:")
msg = f"Olá, {name}! Bom saber que você tem {age} anos. Seja bem vinda(o)!"
print(msg)
# print("Seu nome é", name, "e você tem", age, "anos")
# print("Olá, ", name, "! Bom saber que você tem ", age, " anos. Seja bem vinda(o)!", sep="")

# DEPRECADO
# msg = "Olá, {name}! Bom saber que você tem {age} anos. Seja bem vinda(o)!"
# msg = msg.format(name=name, age=age)
# %%
# EXERCICIO ??
age1 = int(input("Digite a 1a idade:"))
age2 = int(input("Digita a 2a idade:"))

average = (age1 + age2) / 2
print("A média das idades é de", average)
# %%
# EXERCICIO 3
raio = float(input("Digite o raio da circunferência:"))
pi = 3.14
area = round(pi * (raio ** 2), 2)
perimetro = round(2 * (pi * raio), 2)
print(f"A área do raio {raio} é igual a {area} e o perímetro é igual a {perimetro}")

# %%
# EXERCICIO 4
valor1 = float(input("Digite o 1o valor:"))
valor2 = float(input("Digite o 2o valor:"))
soma = round(valor1 + valor2, 2)
print("O resultado da soma de", valor1, "e de", valor2, "é ->", soma)
# %%
# EXERCICIO 5
valor1 = int(input("Digite o 1o valor:"))
valor2 = int(input("Digite o 2o valor:"))
potencia = valor1 ** valor2
print(f"O resultado de {valor1} elevado a {valor2} é -> {potencia}")
# %%
# EXERCICIO 6
nota1 = float(input("Digite a 1a nota:"))
nota2 = float(input("Digite a 2a nota:"))
nota3 = float(input("Digite a 3a nota:"))
nota4 = float(input("Digite a 4a nota:"))
notas = [nota1, nota2, nota3, nota4]
media = round(sum(notas) / len(notas), 2)
minimo = min(notas)
maximo = max(notas)
print("Sua média é ", media, ".", " Sua nota máxima foi ", 
maximo, ".", " E sua menor nota foi ", minimo, sep="")
# %%
 