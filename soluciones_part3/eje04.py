# -*- coding: utf-8 -*-
# función llamada last_value que devuelva el último valor de la lista que se le pasa como parámetro
# si la lista está vacía, o no se le pasa una lista debe devolver None
# si la lista tiene un solo elemento debe devolver ese elemento
# devolverá el elemento convertido a mayusculas solo si el elemento es una cadena de texto

def last_value(elements):
    if not type(elements) == list or len(elements)==0: return None
    last=elements[-1]
    if type(last) == str: return last.upper()
    return last


def test():
    assert last_value([4,6,'Ana']) == 'ANA', "Should be ANA"
    assert last_value([4,6,7]) == 7, "Should be 7"
    assert last_value([4,6,True]) == True, "Should be True"
    assert last_value([]) == None, "0 elements should be None"
    assert last_value(None) == None, "None value should be None"
    assert last_value('casa') == None, "casa value should be None"


if __name__ == "__main__":
    test()
    print("Everything passed")