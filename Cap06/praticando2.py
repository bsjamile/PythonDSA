f = open('arquivos/salarios.csv','r') #modo leitura

data = f.read()

rows = data.split('\n') #Quando encontrar o enter, fazer a divisao do meu arquivo

# print(rows) #transformei tudo em uma unica linha (dentro de uma lista)

full_data = []
count = 0

for row in rows:
    split_row = row.split(',')
    full_data.append(split_row)
    count+=1
print(full_data)
print('Esse arquivo tem %s linhas'%(count))
