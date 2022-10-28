# Crea función llamada myValue que devuelva un número decimal negativo

###### pon aquí tu código

def myValue():
    return -1.

def test():
    assert myValue() < 0, "Should be lower to 0"
    assert type(myValue()) is float, "should be a decimal"

if __name__ == "__main__":
    test()
    print("Everything passed")