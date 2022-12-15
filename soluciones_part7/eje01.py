# -*- coding: utf-8 -*-
# Crea una función llamada get_price_final muestre cuanto valen todos los productos (su suma) guardados en el fichero datos.txt

def get_price_final(file):
    f=open(file,'r')
    money=0
    for line in f:
        price = line.split(';')[1]
        money += float( price.split(':')[1] )
    f.close()
    return money

def test():
    assert get_price_final('soluciones_part7/datos.txt') == 19.77, "All products should be 19.77 €"

if __name__ == "__main__":
    test()
    print("Everything passed")