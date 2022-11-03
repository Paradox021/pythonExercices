# -*- coding: utf-8 -*-
# Guarda en una variable llamada my_set (de tipo set) los valores, 5, 6, "verde", "rojo", 7, 6
# ¿Cuantos elementos tienes guardados?

mySet = ????

def test():
    assert type(mySet) == set, "Should be a set"
    assert len(mySet) == 5, "Should be 5 elements"
    assert (5 in mySet) == True, "Should have 5"
    assert (6 in mySet) == True, "Should have 6"
    assert ("verde" in mySet) == True, "Should have verde"
    assert ("rojo" in mySet) == True, "Should have rojo"
    assert (7 in mySet) == True, "Should have 7"


if __name__ == "__main__":
    test()
    print("Everything passed")