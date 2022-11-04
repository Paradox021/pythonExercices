# -*- coding: utf-8 -*-
from calendar import TextCalendar
from curses.textpad import Textbox
import math

# De la siguiente cadena de texto
text = "Hoy es un buen día"

#Guarda en una variable llamada v1 los ultimos 3 caracteres
v1=  ????

#Guarda en una variable llamada v2 los 6 primeros caracteres
v2=  ????


#Guarda en una variable llamada v3 los caracteres desde la posicion 11 a la 14 inclusive
v3=  ????


def test():
    assert v1=='día', "Should be dia"
    assert v2=='Hoy es', "Should be hoy es"
    assert v3=='buen', "Should be buen"

if __name__ == "__main__":
    test()
    print("Everything passed")