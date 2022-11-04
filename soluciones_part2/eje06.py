# -*- coding: utf-8 -*-

# Dado un dni ej 36723445n , devolver solo la letra correspondiente en mayúsculas.
# Crea para ello una función llamada get_dni_letter
# Si el dni no tiene 9 caracteres, devolver None
# Si el dni no tiene una letra en la última posición ( isalpha() ), devolver None
def get_dni_letter(dni):
    if len(dni) != 9: return None
    if not dni[-1].isalpha(): return None
    return dni[-1].upper()


def test():
    assert get_dni_letter('36723445n') == 'N', "Should be N"
    assert get_dni_letter('36723445N') == 'N', "Should be N (upper)"
    assert get_dni_letter('36633456e') == 'E', "Should be E"
    assert get_dni_letter('33') == None, "Should be none (too short)"
    assert get_dni_letter('2342342524523452n') == None, "Should be none (too long)"
    assert get_dni_letter('366334567') == None, "Should be none no letter"

if __name__ == "__main__":
    test()
    print("Everything passed")