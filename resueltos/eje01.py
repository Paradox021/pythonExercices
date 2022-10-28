# La función returnValue deberá devolver un 6
# Comenta las lineas de código adecuadas
# usando 2 tipos diferentes de comentarios

def returnValue():
    
    #a=5
    
    b=6
    '''
    b=a+6
    b=b+7
    '''
    return b


def test():
    assert returnValue() == 6, "Should be 6"

if __name__ == "__main__":
    test()
    print("Everything passed")