# -*- coding: utf-8 -*-
# crea una función llamada suma_10 que determine si hay 2 valores cualesquiera en la lista que sumen 10
# El reto está en crear una algoritmo con complejidad O(n). (Un solo bucle for)

# O(n)
def suma_8(list):
    # your code here
    return False

def test():
    f = open(__file__, 'r')
    assert f.read().split(' ').count('for')==1, "Should have 1 bucle for"
    assert suma_8([1,3,6,9]) == False, "No 2 numbers sum 8"
    assert suma_8([1,6,2,10]) == True, "Yes 6+2 = 8"
    assert suma_8([1,6,3,10,3,4,6,2,12,3,4,5]) == True, "Yes sum  8"

if __name__ == "__main__":
    test()
    print("Everything passed")