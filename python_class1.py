# Databricks notebook source
# %%
print("hello, queen")

# COMMAND ----------

# DBTITLE 1,Variables
# %%
name = "Queen"
type(name)
# %%

name = input("Digite seu nome: ")
print(name)
#%%
name = input("Digite seu nome: ") # pode ser aspas simples também
print("Seu nome é:", name)
# %%
texto_longo = ''' Este é um texto longo 
e que pode ser utilizado com aspas simples 3x
'''
print(texto_longo)
# %%

print("1 + 1 =", 1+1)
print("2 - 1 =", 2-1)
print("10 x 2 =", 10*2)
print("10 / 3 =", 10/3)
print("10 % 3 =", 10%3)
print("10 // 3 =", 10//3)
print("10**2 =", 10**2)
print("4**(1/2)", 4**(1/2))
print("True", True)
print("False", False)
print("True + True =", True + True)
print("True + False =", True + False)
# %%
raio = 1
pi = 3.14
area = pi * (raio ** 2)
print("Área é igual a", area)
# %%
