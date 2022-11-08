# -*- coding: utf-8 -*-
# función llamada consecutive_suma_10 que determine si hay 2 valores consecutivos en la lista que sumen 10
# # pueden ser enteros y decimales
def consecutive_suma_10(list): 
    # your code here
    return None

def test():
    assert consecutive_suma_10([1,4,6,5,5]) == True, "5+5 Should be true"
    assert consecutive_suma_10([1,4,2.5,7.5,5]) == True, "2.5 + 7.5 Should be true"
    assert consecutive_suma_10([5,5,2.5,7,5]) == True, "5+5 Should be true"
    assert consecutive_suma_10([1,4,2.5,8,5]) == False, "Should be False"
    assert consecutive_suma_10([]) == False, "Should be False"
    assert consecutive_suma_10([10]) == False, "Should be False"
    assert consecutive_suma_10([10,10]) == False, "Should be False"


if __name__ == "__main__":
    test()
    print("Everything passed")