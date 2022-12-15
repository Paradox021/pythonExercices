# -*- coding: utf-8 -*-

# Usando la tecnica de List Comprehension
# Crea una función llamada dog_filter a la que se le pase un array con nombres de perros.
# Esta función devolverá un array solo con los nombres de los perros que contengan la letra 's'
# Esos nombres se devolverán en mayúsculas

def dog_filter(names):
    pass

def test():
    assert dog_filter(["pipo", "doggy", "flash", "kenny", "sugus"])==['FLASH', 'SUGUS'], "error filte flash and sugus"
    assert dog_filter(["rapid", "goffy", "kid", "star"])==['STAR'], "error filter star"
    assert dog_filter(["rapid", "goffy", "kid", "guld"])==[], "error filter empty"

if __name__ == "__main__":
    test()
    print("Everything passed")