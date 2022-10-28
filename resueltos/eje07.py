# La función calculus devuelve 3 valores
# guarda los 2 primeros valores 
# en dos variables llamadas value1 y value 2
# hazo en una sola linea

def calculus():
    return 3.1415, 2.718 

###### pon aquí tu código
value1, value2 = calculus()

def test():
    assert value1 == 3.1415, "value1 hould be 3.1415"
    assert value2 == 2.718, "value2 Should be 2.718"

if __name__ == "__main__":
    test()
    
    print("Everything passed")