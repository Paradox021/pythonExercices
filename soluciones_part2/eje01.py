# -*- coding: utf-8 -*-

# Crea función llamada expo que devuelva un número elevado a un valor

def expo(a,b):
    return a**b


def test():
    assert expo(2,3) == 8, "2^3 Should be 8"
    assert expo(3,2) == 9, "3^2 should be 9"
    assert expo(10,0) == 1, "10^0 should be 1"


if __name__ == "__main__":
    test()
    print("Everything passed")