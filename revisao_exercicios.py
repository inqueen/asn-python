# %%
# EXERCICIO 7

from re import A


lista = [120, "Python", 120.01, "asn", False, [10,20] ]

print(lista[-1])
print(lista[0])
print(lista[1][-1])
# %%

segundos = int(input("Digite um número em segundos:"))

horas = segundos // (60*60)
segundos = segundos % (60*60)

minutos = segundos // (60)
segundos = segundos % (60)

texto = f"{horas:0>2}:{minutos:0>2}:{segundos:0>2}"
print(texto)

# Entrada: 556
# Saída: 0:9:16
# Entrada: 140153
# Saída: 38:55:53

# %%
# DESCOMPRESSÃO DE LISTAS

notas = [1.5, 2.4, 3.9]
n1, n2, *_ = notas 
# *_ é uma boa prática para desconsiderar variáveis que não vai usar
# * se chama coringa 
# *_ pode ser usado em qualquer parte da lista
print(n2)

# %%

a = 10
b = 20

a, b = b, a

print(a, b)
# %%

a, b, c, *_ = "abcdefghijklmnopqrstuvwyxz"
print(_)
# %%
