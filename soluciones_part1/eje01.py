# La función return_value deberá devolver un 6
# Comenta las lineas de código adecuadas
# usando 2 tipos diferentes de comentarios

def return_value():
    #a=5
    b=6
    '''b=a+6
    b=b+7'''
    return b


def test():
    assert return_value() == 6, "Should be 6"

if __name__ == "__main__":
    test()
    print("Everything passed")