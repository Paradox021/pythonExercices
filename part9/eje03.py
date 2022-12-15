# -*- coding: utf-8 -*-

# Crea manualmente otro fichero llamado utils.py
# En ese fichero (utils.py) crea una función llamada is_currency(money) que:
# Mediante expresiones regulares comprueba si un texto tiene el formato de moneda:
# - Tendrá que tener 2 decimales obligatorios
# - El separador de decimales será el punto
# - No se usará el separador de miles
# - Deberá terminar con el simbolo en €

# Importa la función is_currency en este fichero

def test():
    assert is_currency('123.453')==False, "Finish with €"
    assert is_currency('123.45€')==True, "Error en el test 1"
    assert is_currency('122343.45€')==True, "Error en el test 1"
    assert is_currency('123.4€')==False, "2 decimals you pass 1"
    assert is_currency('123.453€')==False, "2 decimals you pass 3"
    assert is_currency('1,236.45€')==False, "2 decimals you pass 3"
    assert is_currency('123')==False, "2 decimals you pass 0"

if __name__ == "__main__":
    test()
    print("Everything passed")