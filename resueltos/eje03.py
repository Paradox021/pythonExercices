# Crea función llamada cube que se le pasa como parámetro
# un valor y devuelve el mismo elevado al cubo

###### pon aquí tu código

def cube(num):
    return num ** 3

def test():
    assert cube(2) == 8, "Should be lower 2^3 to 8"

if __name__ == "__main__":
    test()
    print("Everything passed")