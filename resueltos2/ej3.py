# -*- coding: utf-8 -*-

# Los productos de un almacen se han dividido en dos grupos A y B de acuerdo a: si caduca y su nombre. 
# El grupo A esta formado por los caducables cuyo nombre sea anterior a la 'm' y los no caducables con un nombre posterior a la 'n'
# y el grupo B por el resto. 
# Escribir una función llamada get_group que se le pase si es caducable(booleano) y su nombre(string), y devuelva el grupo que le corresponde 'A' o 'B'.
# Intenta usar un solo if (sin else)

###### pon aquí tu código

def get_group(b, cad):
    if b:
        if 'm' > cad[0]:
            return 'A'
        return 'B'
    if 'm' < cad[0]:
        return 'A'
    return 'B'

def test():
    assert get_group(True, 'bic') == "A", "True, 'bic' Should be A"
    assert get_group(True, 'mouse') == "B", "True, 'mouse' Should be B"
    assert get_group(False, 'orange') == "A", "False, 'orange' Should be A"
    assert get_group(False, 'glue') == "B", "False, 'glue' Should be B"

if __name__ == "__main__":
    test()
    print("Everything passed")