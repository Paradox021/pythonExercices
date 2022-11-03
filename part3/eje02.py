# -*- coding: utf-8 -*-
# Crea una colección de 4 elementos
# El primer elemento debe ser un número entero
# El segundo elemento debe ser una cadena de texto
# El tercer elemento debe ser un valor booleano
# El cuarto elemento debe ser una lista de 3 elementos de tipo cadena de texto

colection = ???


def test():
    assert len(colection) == 4, "Should be 4 elements"
    assert type(colection[0]) is int, "first element should be int"
    assert type(colection[1]) is str, "second element should be string"
    assert type(colection[2]) is bool, "third element should be bool"
    assert type(colection[3]) is list, "fourth element should be list"
    assert len(colection[3]) == 3, "fourth element should be 3 element"
    assert type(colection[3][0]) is str, "first element of fourth element should be string"
    assert type(colection[3][1]) is str, "second element of fourth element should be string"
    assert type(colection[3][2]) is str, "third element of fourth element should be string"


if __name__ == "__main__":
    test()
    print("Everything passed")