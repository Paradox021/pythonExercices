# -*- coding: utf-8 -*-
# crea una función llamada remove_duplicates(data) que reciba una lista y devuelva otra lista sin elementos duplicados
# no uses ni condicionales ni bucles

flowers = ['rosa','crisantemo','gladiolo','margarita','rosa','gladiolo','jacinto','rosa','gardenia']

def remove_duplicates(data):
    # your code here
    lista = list(set(data))
    return lista

def test():
    assert remove_duplicates(['pera', 'limon', 'fresa', 'pera', 'limon', 'limon']).count('pera')==1, "Should be 1 pera"
    assert remove_duplicates(['pera', 'limon', 'fresa', 'pera', 'limon', 'limon']).count('limon')==1, "Should be 1 pera"
    assert remove_duplicates(['pera', 'limon', 'fresa', 'pera', 'limon', 'limon']).count('fresa')==1, "Should be 1 pera"


if __name__ == "__main__":
    test()
    print("Everything passed")