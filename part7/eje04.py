# -*- coding: utf-8 -*-
# Crea una funcion llamada my_filter que reciba una lista de numeros.
# Esta devolverá una lista con los numeros pares que sean mayor de 5,
# además de multiplicarlos por 2



def my_filter(numbers):
    pass

def test():
    assert my_filter([-5,-3,0,2,3,5,7,8,9])== [16], "filtered should be 8x2 = 16"
    assert my_filter([-5,-3,0,2,3,5,7,8,9,6])== [16,12], "filtered should be 8x2=16 and 6x2=12 [16,12]"
    assert my_filter([])== [], "empty list should be []"
    assert my_filter([9])== [], "[9] should be []"
    assert my_filter([10])== [20], "[10] should be [20]"

if __name__ == "__main__":
    test()
    print("Everything passed")