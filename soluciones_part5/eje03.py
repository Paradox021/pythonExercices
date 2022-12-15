# -*- coding: utf-8 -*-
# funcion llamada have_negatives que reciba una lista de números y devuelva True si hay algún número negativo en la lista
# En otro caso, o si no se le pasa una lista de numeros devolverá falso
def have_negatives(numbers):
    if type(numbers) != list: return False
    for i in numbers:
        if type(i) != int and type(i) != float: return False
        if i < 0: return True
    return False


def test():
    assert have_negatives([1,4,6,5,5]) == False, "No negatives"
    assert have_negatives([1,4,6,-5,5]) == True, "Yes -5 is negative"
    assert have_negatives([]) == False, "empty no negatives"
    assert have_negatives('hola') == False, "empty no negatives"


if __name__ == "__main__":
    test()
    print("Everything passed")