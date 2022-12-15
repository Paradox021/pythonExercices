# -*- coding: utf-8 -*-

# Crea una funcion llamada more_long que reciba varias palabras y
# devuelva la palabra que tenga más letras.
# Si no se pasan palabras debe devolver None
# Si se pasan varias palabras con el mismo numero de letras debe devolver la primera que encuentre

def more_long(*args):
    if len(args)==0: return None
    #return max(args, key=len)
    max=args[0]
    for a in range(1,len(args)):
        if len(args[a]) > len(max):
            max=args[a]
    return max

def test():
    assert more_long('ana','ana','ana')=='ana', "The second parameter must be an string1"
    assert more_long('ana','juana','pio','rosa','pedro')=='juana', "The second parameter must be an string1"
    assert more_long('ana','juana','pio','isabelina')=='isabelina', "The second parameter must be an string2"
    assert more_long()==None, "The second parameter must be an string3"

if __name__ == "__main__":
    test()
    print("Everything passed")