# Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.
lista = []

for i in range(1,11):
    lista.append(i)
print(lista)

# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela

lista2 = []

for i in range(1,6):
    lista2.append(i)
print(lista2)

# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string

nome = 'Jamile'
sobrenome = 'Barroso'
nome_completo = f'{nome} {sobrenome}'
print(nome_completo)

# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do 
# objeto tupla para verificar quantas vezes o número 4 aparece na tupla

tupla = (1, 2, 2, 3, 4, 4, 4, 5)
quatro = tupla.count(4)
dois = tupla.count(2)
print(f'O número 4 aparece {quatro}x e o número 2 aparece {dois}x!')

# Exercício 5 - Crie um dicionário vazio e imprima na tela

dicionario = {}
print(dicionario)

# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela

dicionario = {'Jamile':29,'Dani':34,'Lucas':28,'Romão':41}
print(dicionario)

# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela
dicionario['André'] = 34
print(dicionario)

# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. 
# Um dos valores deve ser uma lista de 2 elementos numéricos. 
# Imprima o dicionário na tela.

dicionario2 = {'Jamile':3.6,'Dani':5.8,'Lista':[0,2]}
print(dicionario2)

# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string, 
# o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e 
# o quarto elemento um valor do tipo float.
# Imprima a lista.

lista3 = ['Jamile',(1,3),{'José':31,'Trindade':33},3.5]
print(lista3)

# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.
frase = 'Cientista de Dados é o profissional mais sexy do século XXI'
ate_dezoito = frase[:18]
print(ate_dezoito)