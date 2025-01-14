# -*- coding: utf-8 -*-

# Crea una función llamada birthday, que pasándole tu año de nacimiento 
# y el año actual, devuelva la frase: 
#   tienes xx años.
# No se tendrán en cuenta los meses (solo los años), deberás usar un string formateado


###### pon aquí tu código

def birthday(n1, n2):
    edad = n2-n1
    return "tienes {} años".format(edad)


def test():
    assert birthday(2000, 2021) == "tienes 21 años", "Should be 21 years"
    assert birthday(2000, 2020) == "tienes 20 años", "Should be 20 years"
    assert birthday(2000,2000) == "tienes 0 años", "should be 0 years"


if __name__ == "__main__":
    test()
    print("Everything passed")