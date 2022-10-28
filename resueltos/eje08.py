# ejecuta la siguiente instrucción en la consola:
# pip install mock

# Crea una función access
# esta deberá pedir por teclado la edad de una persona
# si esta es menor de edad le mostrará la frase: 'Acceso denegado'
# si esta es mayor de edad le mostrará la frase: 'Acceso permitido'




import mock

def access():
    edad = input("Dame tu edad:")
    if int(edad)>=18:
        return 'Acceso permitido'
    return 'Acceso denegado'

def test():
    with mock.patch('builtins.input', return_value="22"):
        assert access() == "Acceso permitido"

    with mock.patch('builtins.input', return_value="13"):
        assert access() == "Acceso denegado"

if __name__ == "__main__":
    test()
    print("Everything passed")