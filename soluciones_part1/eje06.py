# Crea una funcion llamada character_counter que reciba
# como parámetro una frase y devuelva su nº de caracteres

###### pon aquí tu código

def character_counter(text):
    if type(text) != str: return 0
    return len(text)

def test():
    assert character_counter('Hola') == 4, "Should be 4"
    assert character_counter('') == 0, "Should be 0"
    assert character_counter(None) == 0, "Should be 0"

if __name__ == "__main__":
    test()
    print("Everything passed")