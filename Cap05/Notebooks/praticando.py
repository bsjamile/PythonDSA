#%%
def addNum(num1, num2):
    print(f"Primeiro: {num1}")
    print(f"Segundo: {num2}")
    print(f"Soma: {num1+num2}")
# %%
addNum(4,5)
# %%
addNum(45,90)
# %%
def printNum():
    for num in range (1,11):
        print(f"Número: {num}")
# %%
printNum()
# %%
def printVarInfo(arg1, *vartuple):
    print("O parâmetro passado foi: ", arg1)

    for item in vartuple:
        print("O parâmetro passado foi: ", item)
    return;
# %%
printVarInfo("Morango","Mamão")
# %%
printVarInfo(1,2,3)
# %%
printVarInfo(100)
# %%
idade = int(input("Qual a sua idade? "))
if idade >= 13:
    print(f"{idade} é maior ou igual a 13")
else:
    print(f"{idade} é menor que 13")
# %%
# Funções Built-in (funções pre prontas)
len([1,2,3,4])
# %%
array = [5,6,7]
max(array)
# %%
min(array)
# %%
lista = [16,23,38,66]
sum(lista)
# %%
import math

def numPrimo(num):
    if (num % 2) == 0 and num > 2:
        return "Este número não é primo"
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if (num % i ) == 0:
            return "Esse número não é primo"
    return "Este número é primo"

# %%
numPrimo(2)
# %%
numPrimo(389)
# %%
numPrimo(4)
# %%
caixa_baixa = "Este Texto Deveria ESTAR TODO EM LOWERCASE"
# %%
def lowercase(text):
    return text.lower()
# %%
lowercase_string = lowercase(caixa_baixa)
# %%
lowercase_string
# %%
def split_string_palavras(text):
    return text.split(" ")
# %%
meu_nome = "Jamile Barroso dos Santos"
# %%
split_string_palavras(meu_nome)
# %%
print(split_string_palavras(meu_nome))
# %%
# token - menor estrututura que pode chegar dentro de um texto (palavras)
texto = "Esta função será BASTANTE ÚTIL PARA separar grandes VOlumes de DaDos"
token = split_string_palavras(texto)
# %%
token
# %%
def split_string_letras(text):
    texto = text.upper()
    for letra in texto:
        print(letra)
# %%
split_string_letras("Jamile")
# %%
amor = "Alberlene"
split_string_letras(amor)
# %%
split_string_letras(texto)

# %%
# Expressao lambda
def potencia(num):
    resultado = num ** 2
    return resultado
# %%
potencia(5)
# %%
def potencia(num): return num ** 2
# %%
potencia = lambda num: pow(num,2)

# %%
potencia(2)
# %%
Par = lambda x: x%2==0
# %%
Par(5)
# %%
Par(4)
# %%
first = lambda s: s[0]
# %%
first("Jamile")
# %%
reverso = lambda t: t[::-1]
# %%
reverso("Python")
# %%
addNum = lambda x,y: x+y
# %%
addNum(2,3)
# %%
[x for x in range(10)]
# %%
lista_numeros = [x for x in range(21)]
# %%
print(lista_numeros)
# %%
lista2_numeros = [x for x in range(10) if x <= 5]
# %%
lista2_numeros
# %%
lista_frutas = ["banana","abacate","melancia","maçã"]
# %%
lista_nova = []
# %%
for x in lista_frutas:
    if "m" in x:
        lista_nova.append(x)
        
print(lista_nova)
# %%
nova_lista = [x for x in lista_frutas if "m" in x]
print(nova_lista)
# %%
dict_alunos = {'Bob':68, 'Michel':84,'Zico':57,'Ana':93}

dict_alunos_status = {k:v for (k,v) in dict_alunos.items()}
print(dict_alunos_status)
# %%
dict_alunos_status2 = {k:('Aprovado' if v > 70 else 'Reprovado') for (k,v) in dict_alunos.items()}
print(dict_alunos_status2)
# %%
nome = 'Alberlene'
contador = sum(1 for letra in nome if letra == 'e')
print(f'{nome} tem {contador}x a letra e!')
# %%
ask = input('Qual o dia da semana? ')

ask = ask.lower()

if ask == 'domingo' or ask == 'sábado':
    print('Hoje é dia de descanso!')
else:
    print('Você precisa trabalhar!')
# %%
lista = ['Mamao','Banana','Pera','Uva','Morango']

for morango in lista:
    morango = morango.lower()
    if morango == 'morango':
        print('Morango está na lista!')

# %%
