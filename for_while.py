# %%
num = 1

while num <= 10: 
    print(num)
    num += 1
print("Muito bem!")
# %%
num = 1
while True: 
    print("queen bey")
    if num == 2:
        print("Parando o while")
        break
    num += 1
print("Parou")
# %%
num = 0
while True: 
    num += 1
    print(f"queen bey {num}")

    if num % 2 == 0:
        continue

    if num == 5:
        print("Parando o while")
        break

print("Parou")
# %%
num = 0
while num <= 3: 
    num += 1
    print(f"queen bey {num}")

    if num % 2 == 0:
        continue

    if num == 5:
        print("Parando o while")
        break

else: 
    print("Parou com sucesso (while, linha 33)")
# %%
word = "beyonce"

for abc in word:
    print(abc)
# %%
num = [1,2,3,4,5,6]

for n in num:
    print(n**2)

# %%
for n in range(1,11):
    print(n)
# %%
for n in range(1,11):
    if n % 2 == 0:
        print(f"{n} é par")
    else: 
        print(f"{n} é ímpar")

# %%
for n in range(1,11):
    if n % 2 == 0:
        print(f"{n} é par")
    else: 
        print(f"{n} é ímpar")
    if n == 9: 
        break
print("Acabou o range!")
# %%
x = []

for n in range(1,11):
    x.append(n**2)
print(x)
# %%
x = [n**2 for n in range(1,11)]
print(x)
# %%
x = []

for n in range(1,11):
    if n % 3 != 0:
        x.append(n**2)
print(x)
# %%
x = [n**2 for n in range(1,11) if n % 3 != 0]
print(x)

# tempo de execução é muito menor 
# %%
try: 
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        print(f"{num} é um número par")
    else:
        print(f"{num} é um número ímpar")

except ValueError as err:
    print("Não seja vacilão! Digite um número válido!")
    print(err)
# %%
def number():
    try: 
        num = int(input("Digite um número: "))
        return num
    except ValueError as err:
        print("Não seja vacilão! Digite um número válido (ex.: 1, 2, 30)!")

num = None
while num is None:
    num = number()

if num % 2 == 0:
    print(f"{num} é um número par")
else:
    print(f"{num} é um número ímpar")
# %%
