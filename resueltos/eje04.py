# Crea función llamada evaluator.
# Esta función recivirá un numero por parametro
# que devuelva el booleano true si el numero pasado es mayor de 0, 
# que devuelva false si el numero pasado es menor que 0 
# y que devuelva la palabra 'cero' si el número es igual a 0
# si no se le pasa un número válido tambien deberá devolver 'cero'

###### pon aquí tu código

def evaluator(num):
    if num==0 or type(num) != int and type(num) != float:
        return 'cero'
    return num>0

def test():
    assert evaluator(4) == True, "4 should be true"
    assert evaluator(4.4) == True, "4.4 should be true"
    assert evaluator(-4) == False, "-4 should be false"
    assert evaluator(0) == 'cero', "0 should be true"
    assert evaluator('casa') == 'cero', "casa should be cero"
    assert evaluator(None) == 'cero', "none should be cero"

if __name__ == "__main__":
    test()
    print("Everything passed")