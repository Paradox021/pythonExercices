# -*- coding: utf-8 -*-

# Crea una función que sume todos los digitos de un número hasta obtener un solo dígito
# Por ejemplo: 2424 = 2 + 4 + 2 + 4    =     12    = 1 + 2     = 3
def suma_de_digitos_iterativa(num):
    pass

def test():
    assert suma_de_digitos_iterativa(0) == 0, "0 should be 0"
    assert suma_de_digitos_iterativa(5) == 5, "5 should be 5"
    assert suma_de_digitos_iterativa(2424) == 3, "2424 should be 3"
    assert suma_de_digitos_iterativa(458759545485) == 6, "458759545485 should be 6"
    assert suma_de_digitos_iterativa(75124365485544) == 9, "75124365485544 should be 9"

if __name__ == "__main__":
    test()
    print("Everything passed")