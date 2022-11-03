# -*- coding: utf-8 -*-
# Guarda en una nueva variable llamada inverse_fruits la lista fruits pero al revés


fruits = ['🍑', '🍊', '🍋', '🍓']

inverse_fruits = fruits[::-1]
###### pon aquí tu código


def test():
    assert fruits == ['🍑', '🍊', '🍋', '🍓'], 'fruits should be unchanged'
    assert inverse_fruits == ['🍓','🍋', '🍊', '🍑'], 'inverseFruits should be reversed'


if __name__ == "__main__":
    test()
    print("Everything passed")