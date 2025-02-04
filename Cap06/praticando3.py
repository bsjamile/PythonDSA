arq3 = open('arquivos/arquivo3.txt', 'w')
arq3.write('''Este arquivo foi gerado automaticamente.''')
arq3.write('\nO curso DSA é mto legal!')
arq3 = open('arquivos/arquivo3.txt', 'r')

print(arq3.read())
arq3.seek(0)
print(arq3.readlines())

arq3.close()

for line in open('arquivos/arquivo3.txt'):
    print(line)
# praticando = open('arquivos/arquivo4.txt','w')
# praticando.write('Olá, Mundo!')