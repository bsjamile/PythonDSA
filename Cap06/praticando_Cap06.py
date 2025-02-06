# %%
# Exercício 1 - Crie uma lista de 3 elementos e calcule a terceira potência de cada elemento.

lista_pow = [3,9,22]

list(map(lambda x:x**3,lista_pow))

# %%
# Exercício 2 - Reescreva o código abaixo, usando a função map(). O resultado final deve ser o mesmo!
palavras = 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil.'.split()
# resultado = [[w.upper(), w.lower(), len(w)] for w in palavras]
# for i in resultado:
#     print (i)


palavras2 = 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil.'
def solve(x):
    resultado = [[w.upper(), w.lower(), len(w)] for w in x]
    for i in resultado:
        print (i)
list(map(solve,palavras))
# %%
# Exercício 3 - Calcule a matriz transposta da matriz abaixo.
# Caso não saiba o que é matriz transposta, visite este link: https://pt.wikipedia.org/wiki/Matriz_transposta
# Matriz transposta é um conceito fundamental na construção de redes neurais artificiais, base de sistemas de IA.
matrix = [[1, 2],[3,4],[5,6],[7,8]]


# %%
# Exercício 4 - Crie duas funções, uma para elevar um número ao quadrado e outra para elevar ao cubo. 
# Aplique as duas funções aos elementos da lista abaixo. 
# Obs: as duas funções devem ser aplicadas simultaneamente.
lista = [0, 1, 2, 3, 4]

def quadrado(x):
    resultado = x ** 2
    return resultado
def cubo(y):
    resultado = y ** 3
    return resultado

print(list(map(lambda x: (quadrado(x),cubo(x)),lista)))

print(list(map(lambda x: ((lambda y: y **2)(x),(lambda w: w **3)(x)),lista)))

# %%
# Exercício 5 - Abaixo você encontra duas listas. Faça com que cada elemento da listaA seja elevado 
# ao elemento correspondente na listaB.
listaA = [2, 3, 4]
listaB = [10, 11, 12]

def eleva(x,y):
    result = x**y
    return result

print(list(map(eleva, listaA, listaB)))

print(list(map(lambda x, y : x ** y, listaA, listaB)))


# %%
# Exercício 6 - Considerando o range de valores abaixo, use a função filter() para retornar 
# apenas os valores negativos.
valores = range(-5, 5)

lista = [-6, -3, 0, 2, 4, 6, -4, -1]

list(filter(lambda x: x < 0,valores))


list(filter(lambda x: x in range(-5,5) and x < 0,lista))

# %%
# Exercício 7 - Usando a função filter(), encontre os valores que são comuns às duas listas abaixo.
a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]

list(filter(lambda x: x in b,a))
# %%
# Exercício 8 - Considere os dois dicionários abaixo. 
# Crie um terceiro dicionário com as chaves do dicionário 1 e os valores do dicionário 2.
dict1 = {'a':1,'b':2}
dict2 = {'c':4,'d':5}

dict3 = {}

# dict3.update(dict1)
# dict3.update(dict2)
dict3 = list(zip(dict1,dict2.values()))

print(dict3)
# %%
# Exercício 9 - Considere a lista abaixo e retorne apenas os elementos cujo índice for maior que 5.
lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

print(list(enumerate(lista)))

for i, item in enumerate(lista):
    if i > 5:
        print(f"Indice {i}: Letra {item.upper()}")

# %%
# Exercício 10 - Crie um regex em Python para extrair a palavra que aparece depois das palavras 
# Data e Science na frase: 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil.'
import re
texto = 'A Data Science Academy oferece os melhores cursos de análise de dados do Brasil.'
resultado = re.findall(r"Data Science\s(.*)", texto) #. significa qlqr caracter e * zero ou mais
print(resultado)
# %%
