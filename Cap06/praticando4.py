# %%
# Importando a função reduce do módulo functools
from functools import reduce
# %%
lista = [47,11,42,13]
# %%
soma = lambda x,y:x+y
reduce(soma,lista)
# %%
def sum(a,b):
    return a+b;
reduce(sum,lista)
# %%
reduce(lambda x,y:x+y,lista)
# %%
max_find = lambda a,b:a if (a>b) else b
# %%
type(max_find)
# %%
reduce(max_find,lista)
# %%
def verificaPar(num):
    if num % 2 == 0:
        return True
    else:
        return False
# %%
verificaPar(35)
# %%
lista4 = [1,2,3,4,16,28,36,50]
# %%
verificando = lambda num: num%2 == 0
# %%
list(filter(verificando,lista4))
# %%
list(filter(verificaPar,lista4))
# %%
list(filter(lambda num: num > 8, lista4))
# %%
x = [1,2,3]
y = [4,5,6]
zip(x,y)
# %%
list(zip(x,y))
# %%
# Se não consegue combinar, simplesmente descanta
list(zip('ABCD','xy'))
# %%
a = [1,2,3]
b = [4,5,6,7,8]
list(zip(a,b))

# %%
d1 = {'a':1,'b':2}
d2 = {'c':3, 'd':4}
list(zip(d1,d2)) # combina apenas as chaves
# %%
list(zip(d1,d2.values()))
# %%
def trocaValores(d1,d2):
    dicTemp = {}

    for d1key, d2val in zip(d1, d2.values()):
        dicTemp[d1key] = d2val

    return dicTemp
# %%
trocaValores(d1,d2)
# %%
seq = ['a','b','c']
# %%
enumerate(seq)
# %%
list(enumerate(seq)) #indice de cada caractere na lista
# %%
for indice, valor in enumerate(seq):
    print(indice,valor)
# %%
for indice, valor in enumerate(seq):
    if indice >=2:
        break
    else:
        print(valor)
# %%
lista_nome = ['Jamile','Adriele','Daniela']
for i, iten in enumerate(lista_nome):
    print(i,iten)
# %%
for i, iten in enumerate("Data Science Acadamy"):
    print(i,iten)
# %%
for i, iten in enumerate(range(10)):
    print(i,iten)
# %%
