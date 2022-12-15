# -*- coding: utf-8 -*-
# función llamada superstition que reciba una tupla e indique el número de veces que aparece repetido el numero 13
# si a la función no se le pasa una tupla correcta, devolverá 0

def superstition(element):
    if type(element) != tuple: return 0
    return element.count(13)


def test():
    assert superstition( (2,4,5) ) == 0, "should be 0"
    assert superstition( (13,4,5) ) == 1, "should be 1"
    assert superstition( (13,4,13) ) == 2, "should be 2"
    assert superstition( () ) == 0, "empty should be 0"
    assert superstition( None ) == 0, "empty should be 0"
    assert superstition( 'casa' ) == 0, "empty should be 0"


if __name__ == "__main__":
    test()
    print("Everything passed")