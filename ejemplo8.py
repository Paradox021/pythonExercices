

f=open('datos.txt', 'r')

for linea in f:
    print(linea, end='')

f.close()
print('-----------------------------')
with open('datos.txt', 'r') as f:
    for linea in f:
        print(linea, end='')
    f.close()

