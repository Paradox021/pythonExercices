# -*- coding: utf-8 -*-
# Crea una funcion llamada avg que reciba una lista de numeros y devuelva la media de todos ellos
# usa funciones lambda y orden superior

import functools

def avg(numbers):
    f = lambda x,y: x+y
    return functools.reduce(f,numbers)/len(numbers)


def test():
    assert avg([3,4,7,2.3,-1])== 3.06, "avg should be 3.06"

if __name__ == "__main__":
    test()
    print("Everything passed")