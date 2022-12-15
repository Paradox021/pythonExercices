# -*- coding: utf-8 -*-
# Guarda en una nueva variable llamada inverse_fruits la lista fruits pero al revés


fruits = ['🍑', '🍊', '🍋', '🍓']

#inverse_fruits = fruits.copy()
#inverse_fruits=fruits[:]
#inverse_fruits.reverse()
inverse_fruits=fruits[::-1]


def test():
    assert fruits == ['🍑', '🍊', '🍋', '🍓'], 'fruits should be unchanged'
    assert inverse_fruits == ['🍓','🍋', '🍊', '🍑'], 'inverseFruits should be reversed'


if __name__ == "__main__":
    test()
    print("Everything passed")