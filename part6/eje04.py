# -*- coding: utf-8 -*-
# Las variables v1 y v2 calculan el máximo de 2 números
# La variable v2 debe fallar (lanza excepción) ya que no se le pasan 2 enteros
# Modifica el código para que no falle, capturando la excepción y asignando a v2 el valor 0

def max(a, b):
    if not type(a) == int or not type(b) == int:
        raise TypeError("max() argument should be int") 
    if a > b:
        return a
    else:
        return b
    

v1 = max(1, 2)

v2 = max('casa', 1)



def test():
    assert v1 == 2, "v1 Should be 2"
    assert v2 == 0, "v2 Should be 0"


if __name__ == "__main__":
    test()
    print("Everything passed")