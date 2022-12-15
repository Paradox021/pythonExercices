# -*- coding: utf-8 -*-

# Crea una funcion llamada more_long que reciba varias palabras y
# devuelva la palabra que tenga más letras.
# Si no se pasan palabras debe devolver None
# Si se pasan varias palabras con el mismo numero de letras debe devolver la primera que encuentre


def test():
    assert more_long('ana','juana','pio','rosa','pedro')=='juana', "The second parameter must be an string"
    assert more_long('ana','juana','pio','isabelina')=='isabelina', "The second parameter must be an string"
    assert more_long()==None, "The second parameter must be an string"

if __name__ == "__main__":
    test()
    print("Everything passed")