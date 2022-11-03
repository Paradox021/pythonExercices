# Crea función llamada my_value que devuelva un número decimal negativo

###### pon aquí tu código
def my_value():
    return -6.3

def test():
    assert my_value() < 0, "Should be lower to 0"
    assert type(my_value()) is float, "should be a decimal"

if __name__ == "__main__":
    test()
    print("Everything passed")