

## Funciones de orden superior

colection = [-2,5,7,2]

# Funcion pura: 
# - No afecta al exterior 
# - para una entrada siempre da la misma salida
def square(n):
    return n**2

def is_positive(n):
    return n>0

r = list(map(square, colection))
print(r)
r = list(filter(is_positive, colection))
print(r)

r=list(map( lambda n:n**2 ,colection))
print(r)
r=list(filter( lambda n:n>0 ,colection))
print(r)

from functools import reduce
print(reduce(lambda x,y:x+y, colection))