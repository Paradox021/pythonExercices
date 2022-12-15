# -*- coding: utf-8 -*-

# Ejecuta este programa pasandole 2 parametros por la linea de comandos
# El primer parametro debe ser un numero entero
# El segundo parametro debe ser un texto

import sys

def test():
    assert len(sys.argv) == 3, "You must pass 2 parameters"
    assert type(int(sys.argv[1])) == int, "The first parameter must be a integer"
    assert sys.argv[2].isalpha() == True, "The second parameter must be an string"

if __name__ == "__main__":
    test()
    print("Everything passed")