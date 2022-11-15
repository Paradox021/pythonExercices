# -*- coding: utf-8 -*-
# Crea una función llamada numbers(total) que devuelva una lista con los números del 1 al total

def numbers(total):
    # your code here
    lista = []
    for num in range(1, total+1):
        lista.append(num)
    return lista


def test():
    assert type(numbers(4)) == list, "Should be a list"
    assert numbers(4) == [1,2,3,4], "Should be list [1,2,3,4]"


if __name__ == "__main__":
    test()
    print("Everything passed")