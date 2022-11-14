
f=open('datos.txt','r')

texto = f.read()
print(texto, end='')

f.close()

f=open('datos.txt','r')

lines = f.readlines()

print(lines[0], end='')
print(lines[1], end='')

f.close()