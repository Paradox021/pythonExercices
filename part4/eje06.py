# -*- coding: utf-8 -*-
# crea una función llamada getKeys(data) que reciba un diccionario y devuelva una lista con las claves del diccionario
# crea otra función llamada getValues(data) que reciba un diccionario y devuelva una lista con los valores del diccionario

def get_keys(data):
    return ...

def get_values(data):
    return ...


def test():
    assert type(get_keys({'rojo':'bermello', 'amarillo':'amarelo', 'verde':'verde'})) is list, "getKeys Should be a list"
    assert type(get_values({'rojo':'bermello', 'amarillo':'amarelo', 'verde':'verde'})) is list, "getValues Should be a list"
    assert get_keys({'rojo':'bermello', 'amarillo':'amarelo', 'verde':'verde'}) == ['rojo', 'amarillo', 'verde'], "Should be ['rojo', 'amarillo', 'verde']"
    assert get_values({'rojo':'bermello', 'amarillo':'amarelo', 'verde':'verde'}) == ['bermello', 'amarelo', 'verde'], "Should be ['bermello', 'amarelo', 'verde']"


if __name__ == "__main__":
    test()
    print("Everything passed")