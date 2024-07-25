# Exercício 1 - Crie uma estrutura que pergunte ao usuário qual o dia da semana. Se o dia for igual a Domingo ou 
# igual a sábado, imprima na tela "Hoje é dia de descanso", caso contrário imprima na tela "Você precisa trabalhar!"

ask = input('Qual o dia da semana? ')

if ask == 'Domingo' or ask == 'Sábado':
    print('Hoje é dia de descanso!')
else:
    print('Você precisa trabalhar!')

# Exercício 2 - Crie uma lista de 5 frutas e verifique se a fruta 'Morango' faz parte da lista

lista = ['Mamao','Banana','Pera','Uva','Morango']

for morango in lista:
    if morango == 'Morango':
        print('Morango está na lista!')



# Exercício 3 - Crie uma tupla de 4 elementos, multiplique cada elemento da tupla por 2 e guarde os resultados em uma 
# lista

tp = (1,2,3,4)
lista = []

for i in tp:
    i *= 2
    lista.append(i)
print(lista)

# Exercício 4 - Crie uma sequência de números pares entre 100 e 150 e imprima na tela

for i in range(100,151,2):
    print(i)

# Exercício 5 - Crie uma variável chamada temperatura e atribua o valor 40. Enquanto temperatura for maior que 35, 
# imprima as temperaturas na tela

temperatura = 40

while temperatura > 35:
    print(temperatura)
    temperatura -= 1

# Exercício 6 - Crie uma variável chamada contador = 0. Enquanto counter for menor que 100, imprima os valores na tela,
# mas quando for encontrado o valor 23, interrompa a execução do programa

contador = 0

while contador < 100:
    print(contador)
    contador+=1
    if contador == 23:
        break



# Exercício 7 - Crie uma lista vazia e uma variável com valor 4. Enquanto o valor da variável for menor ou igual a 20, 
# adicione à lista, apenas os valores pares e imprima a lista

lista = []
quatro = 4

while quatro <= 20:
    lista.append(quatro)
    quatro +=2
print(lista)


# Exercício 8 - Transforme o resultado desta função range em uma lista: range(5, 45, 2)
# nums = range(5, 45, 2)

lista2 = []

for i in range(5,45,2):
    lista2.append(i)
print(lista2)

# Exercício 9 - Faça a correção dos erros no código abaixo e execute o programa. Dica: são 3 erros.
temperatura = float(input('Qual a temperatura? '))
if temperatura > 30:
    print('Vista roupas leves.')
else:
    print('Busque seus casacos.')

# Exercício 10 - Faça um programa que conte quantas vezes a letra "r" aparece na frase abaixo. Use um placeholder na 
# sua instrução de impressão

# “A gratidão é a virtude das almas nobres. O quão feliz é uma pessoa depende da profundidade de sua gratidão.” 

frase = "A gratidão é a virtude das almas nobres. O quão feliz é uma pessoa depende da profundidade de sua gratidão." 

print(frase)

contador = 0 

for letra in frase:
    if letra == 'r':
        contador+=1
print('Existe %sx a letra r na frase acima!'%(contador))