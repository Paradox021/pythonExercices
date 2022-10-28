# -*- coding: utf-8 -*-

# Crea una función get_type_doc que diferencia entre un nif y un cif
# Si el dni no tiene 9 caracteres, devolver None
# Si noes un nif o cif devolver None
# devolverá la palabra 'NIF' si es un nif y la palabra 'CIF' si es un cif
# Los cif comienzan por la latra de la A a la J

    
###### pon aquí tu código
import re


def get_type_doc(doc):
    regex_nif = "[0-9]{8}([a-z]|[A-Z])"
    regex_cif = "([a-j]|[A-j])[0-9]{8}"
    if(re.match(regex_nif ,doc)):
        return 'NIF'
    if(re.match(regex_cif ,doc)):
        return 'CIF'
    return None

def test():
    assert get_type_doc('23') == None, "Should be N"
    assert get_type_doc('36723445n') == 'NIF', "Should be Nif"
    assert get_type_doc('a36723445') == 'CIF', "Should be cif"
    assert get_type_doc('a3B723445') == None, "Should be none letter B in the middle"
    assert get_type_doc('367Y3445n') == None, "Should be none letter Y in the middle"

if __name__ == "__main__":
    test()
    print("Everything passed")