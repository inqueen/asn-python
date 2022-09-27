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
list_value = []
for i in range(1,5):
    value = int(input(f"Insira suas notas: {i} "))
    list_value.append(value)

media = round(sum(list_value) / len(list_value), 2)
minimo = min(list_value)
maximo = max(list_value)
print("Sua média é ", media, ".", " Sua nota máxima foi ", 
maximo, ".", " E sua menor nota foi ", minimo, sep="")
# %%

# EXERCICIO 2.4
def eh_primo(p=5):
    for i in range(2,p):
        if p % i == 0:
            return False
        return True

num = int(input(f"Entre com um número: "))
# check_primo = eh_primo()

if eh_primo(num):
    print(f"O {num} é primo")

else: 
    print(f"O {num} não é primo")
# %%

# EXERCICIO 2.5
def fib(pos):
    fib_seq = [0,1]

    while True:
        if len(fib_seq) - 1 >= pos:
            return fib_seq[pos]
        else:
            fib_seq.append(fib_seq[-1] + fib_seq[-2])

num = int(input("Digite um número: "))
print(fib(num))
# %%
def fib(pos):
    fib_seq = [0,1]

    while True:
        try:
            return fib_seq[pos]
        except IndexError:
            fib_seq.append(fib_seq[-1] + fib_seq[-2])

num = int(input("Digite um número: "))
print(fib(num))
# %%
# EXERCICIO 2.6

frase = "Esta é a frase original"
frase_lista = frase.split()
frase_nova = ""
for palavra in frase_lista:
    frase_nova += palavra[::-1] + " "
print(frase_nova.lower())
# %%
frase_nova = " ".join([palavra[::-1] for palavra in frase.split()])
print(frase_nova.lower())
# %%
#EXERCICIO 2.7

for num in range(1,101):

    text = ""
    if num % 3 == 0:
        text += "Fizz"
    if num % 5 == 0:
        text += "Buzz"
    if text == "":
        print(num)
    else:
        print(text)
# %%
# EXERCICIO 2.8

def fatorial(num):
    res = 1
    for i in range(2, num + 1):
        res *= 1
    return res
num = int(input(f"Digite um número: "))
fat = fatorial(num)
print(f"O fatorial de {num} é {fat}")


# %%
# EXERCICO 2.9
lista = [123, 435, 987, 1984, 2, 19, 423, -178, 320]

maximo = max(lista)
minimo = min(lista)

valor_max = lista.index(maximo)
valor_min = lista.index(minimo)
print(f"A posição do maior valor é {valor_max} e do menor valor é {valor_min}.")
# %%
