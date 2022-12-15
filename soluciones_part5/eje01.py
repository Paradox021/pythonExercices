# -*- coding: utf-8 -*-
# Crea una función llamada numbers(total) que devuelva una lista con los números del 1 al total

def numbers(total):
    list_result=[]
    for i in range(1,total+1):
        list_result.append(i)
    return list_result


def test():
    assert type(numbers(4)) == list, "Should be a list"
    assert numbers(4) == [1,2,3,4], "Should be list [1,2,3,4]"


if __name__ == "__main__":
    test()
    print("Everything passed")