# -*- coding: utf-8 -*-
# crea una función llamada suma_8 que determine si hay 2 valores cualesquiera en la lista que sumen 8
# El reto está en crear una algoritmo con complejidad O(n). (Un solo bucle for)

# O(n)
#[2,1,8]
#[1,2,8]
# def suma_8(list):
#     f or i in range(len(list)):
#         f or j in range(len(list)):
#             if list[i] + list[j] == 8:
#                 return True
#     return False
def suma_8(list):
    complements = set()
    for e in list:
        if(e in complements): return True
        complements.add(8-e)
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