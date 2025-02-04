f = open('teste.txt','r')

data = f.read()

print(data)

f.seek(0)

print(f.readlines())

f.seek(0)

for line in f:
    print(line)
