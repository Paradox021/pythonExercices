# -*- coding: utf-8 -*-
# Dada una frase, eliminar las partes que están dentro de _


phrase="gato _oso polar_ _leon_ perro _serpiente_ _hiena_"

def readPhrase(phrase):
    # your code here
    return phrase



def test():
    assert readPhrase("hola _como estas_ _yo bien_ gracias ") == "hola   gracias", "You hava 2 ducks"
    pass

if __name__ == "__main__":
    test()
    print("Everything passed")