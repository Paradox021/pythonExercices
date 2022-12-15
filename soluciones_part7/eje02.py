# -*- coding: utf-8 -*-
# Crea una función llamada get_price_of que reciba un diccionario con: 
#   - el nombre del producto 
#   - y los kilos a comprar
# y muestre cuanto es el coste final de la compra

def get_price_of(file, products):
    f=open(file,'r')
    total=0
    for line in f:
        productName=line.split(';')[0].split(':')[1]
        productValue=float(line.split(';')[1].split(':')[1])
        if productName in products:
            total+=productValue*products[productName]
    return total

def test():
    assert round(get_price_of('soluciones_part7/datos.txt', {'kiwi':5, 'naranja':2}), 2 ) == 16.65, "the kiwi and naranja should be 16.65 €"
    assert round(get_price_of('soluciones_part7/datos.txt', {'platano':10}), 2 ) == 13.9, "the platano should be 13.9 €"
    assert round(get_price_of('soluciones_part7/datos.txt', {}), 2 ) == 0, "0 € if no products"

if __name__ == "__main__":
    test()
    print("Everything passed")