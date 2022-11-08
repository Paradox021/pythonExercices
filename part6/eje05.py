# -*- coding: utf-8 -*-
# Crea una clase que represente un password
# La clase debe tener un atributo llamado password
# La clase debe tener un constructror que reciba como parámetro el password
# La clase debe tener un método llamado is_valid() que devuelva True si cumple todo esto:
# - Tiene una longitud mayor o igual a 5
# - no hay 2 digitos iguales adyacentes.
# - De izquierda a derecha los digitos nunca disminuyen
# Crea 2 metodos privados has_two_adjacent_digits y digits_never_decrease para ayudarte a resolver el problema

class Password:
   


def test():
    assert Password('1234').is_valid() == False, "123456 have less than 5 digits"
    assert Password('12345').is_valid() == True, "12345678 have 5 digits, correctly"
    assert Password('123456789').is_valid() == True, "12345678 have 9 digits, correctly"
    assert Password('111111').is_valid() == False, "111111 have two adjacent digits"
    assert Password('3488234').is_valid() == False, "3488234 have two adjacent digits"
    assert Password('12345687').is_valid() == False, "12345687 decrement form 8 to 7"
    assert Password('35679').is_valid() == True, "35679 is a correct password"
    assert hasattr( Password, 'is_valid' ), "Password class should have a is_valid method"
    assert callable( Password.is_valid ), "is_valid can be called"
    assert hasattr( Password, 'has_two_adjacent_digits' )==False, "has_two_adjacent_digits must be private"
    assert hasattr( Password, 'digits_never_decrease' )==False, "has_two_adjacent_digits must be private"

if __name__ == "__main__":
    test()
    print("Everything passed")