# Crea una funcion llamada characterCounter que reciba
# como parámetro una frase y devuelva su nº de caracteres

###### pon aquí tu código

def characterCounter(cad):
    if(type(cad)!=str): 
        return 0
    return len(cad)

def test():
    assert characterCounter('Hola') == 4, "Should be 4"
    assert characterCounter('') == 0, "Should be 0"
    assert characterCounter(None) == 0, "Should be 0"

if __name__ == "__main__":
    test()
    print("Everything passed")