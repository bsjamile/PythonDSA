# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************\n")

print('Selecione o número da operação deseejada: \n')

print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão\n')
try:
    escolha = int(input('Digite sua opção (1/2/3/4): '))
    if escolha >= 1 and escolha <= 4:
        n1 = float(input('Digite o primeiro número: '))

        n2 = float(input('Digite o segundo número: '))

        if escolha == 1:
            conta = n1 + n2
            print(f'{n1} + {n2} = {conta}')
        elif escolha == 2:
            conta = n1 - n2
            print(f'{n1} - {n2} = {conta}')
        elif escolha == 3:
            conta = n1 * n2
            print(f'{n1} * {n2} = {conta:.2f}')
        elif escolha == 4:
            conta = n1 / n2
            print(f'{n1} / {n2} = {conta:.2f}')
    else:
        print('Escolha uma opção válida')
except:
    print('Digite um número inteiro!')



nome = 'Alberlene'
contador = 0
for letra in nome:
    if letra == 'e':
        contador += 1
print(f'{nome} tem {contador}x a letra e!')
