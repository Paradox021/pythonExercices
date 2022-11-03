#Crea una funcion llamada sub que reste 2 numeros

###### pon aquí tu código
def sub(a,b):
    return a-b
    
def test():
    assert sub(2,2) == 0, "Should be 0"
    assert sub(3,2) == 1, "Should be 1"

if __name__ == "__main__":
    test()
    print("Everything passed")