# %%
def f(x): # assinatura da funcao
    # corpo de funcao
    result = 2*(x**2) - 6*x + 125
    return result

print(f(0))
# %%
def concat(name:str, surname="") -> str:
    '''
Essa função concatena 2 strings
    name: string
    surname: string
    '''
    return f"{name} {surname}".title()
print(concat("dani", "queen"))

# %%
def concat(first:str, last:str, middle=""):
    '''
Essa função concatena 2 strings
    first: string
    last: string
    '''
    return f"{first} {middle} {last}".title()
print(concat("dani", "queen"))
# %%
def soma(*args):
    return sum(args)

print(soma(10, 15, 25, 30))

# %%
def soma(a, *args, ignore_even=False):
    '''
    É possível utilizar o *args com valores 
    obrigatórios "a" e outros como um boolean
    '''
    return sum(args)

print(soma(10, 15, 25, 30))
# %%
def config(teclado, mouse, **kwargs):
    print("Teclado: ", teclado)
    print("Mouse: ", mouse)
    print(kwargs)

config("logitec", "apple", headset="sony")

# %%
