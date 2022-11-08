# -*- coding: utf-8 -*-
# Crea una función a la que le pases un Set, una lista o una tupla, y determine si un elemento determinado está guardado en él
# La función debe llamarse contains_element(data, element)
# Donde data podrá ser de tipo lista, tupla o set, en caso de no serlo se devolverá None

def contains_element(data, element):
    # your code here
    if type(data) is not set and type(data) is not list and type(data) is not tuple:
        return None
    return element in data

def test():
    assert contains_element({2,5},5) == True, "{2,5} Should be True"
    assert contains_element([2,5],5) == True, "[2,5] Should be True"
    assert contains_element((2,5),5) == True, "(2,5) Should be True"
    assert contains_element((2,4),5) == False, "(2,4) Should be False"
    assert contains_element('casa',5) == None, "casa Should be none"
    assert contains_element(None,5) == None, "None Should be none"


if __name__ == "__main__":
    test()
    print("Everything passed")