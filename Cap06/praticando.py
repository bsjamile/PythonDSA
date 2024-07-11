# Abrindo o arquivo para leitura
arq1 = open("arquivos/arquivo1.txt", "r") # r = read

print(arq1.read()) #lê e leva o cursor para o final da leitura

print(arq1.tell()) #conta o número de caracteres

print(arq1.read()) #lê e leva o cursor para o final da leitura por isso na segunda leitura n aparece nada

print(arq1.seek(0,0)) #coloca o cursor no inicio da leitura

print(arq1.read()) #lê e leva o cursor para o final da leitura por isso na segunda leitura n aparece nada

print(arq1.seek(0,0)) #coloca o cursor no inicio da leitura

print(arq1.read(23)) #lê até o caractere 23 e leva o cursor para o final da letra 23

print(arq1.read()) #lê e leva o cursor para o final da leitura por isso na segunda leitura n aparece nada

arq2 = open('arquivos/arquivo2.txt','w') #w = write abre para escrever
#se nao encontrar o arquivo2, ele vai criar o arquivo e se ja existir, vai sobreescrever

#Como abrimos o arquivo apenas para gravação, não podemos usar comandos de leitura. "arq2.read()"

arq2.write("Aprendendo a programar em Python.")
arq2.close()

arq2 = open('arquivos/arquivo2.txt','r')

print(arq2.read())

arq2 = open('arquivos/arquivo2.txt','a') #Acrescentando conteúdo (append = acrescentar)

arq2.write(' E a metodologia de ensino da Data Science Academy facilita o aprendizado.')

arq2.close()

arq2 = open('arquivos/arquivo2.txt','r')

print(arq2.read())

arq2.seek(0,0)

print(arq2.read())