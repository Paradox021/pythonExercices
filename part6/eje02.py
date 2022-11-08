# -*- coding: utf-8 -*-
# Crea una función que determine si un número pasado como parámetro es primo.
# La función debe llamarse is_prime(number)
# La función debe devolver True si el número es primo, False en caso contrario
# Si el número no es un entero, o no se le pasa ningún parámetro, debe lanzar una excepción

def is_prime(number):
    # your code here
    return False





import unittest
  
class MyTestCase(unittest.TestCase):
  
    def test_1(self):
        assert type(is_prime(5)) is bool, "should be return boolean"
        assert is_prime(5) == True, "5 should be prime"
        assert is_prime(4) == False, "4 should not be prime"
        assert is_prime(1) == False, "1 should not be prime"

        with self.assertRaises(Exception):
            is_prime('casa')
            is_prime(None)
  
if __name__ == '__main__': 
    unittest.main()
