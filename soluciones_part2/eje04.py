# -*- coding: utf-8 -*-

# Un producto paga obtiene un descuento en función de la cantidad del mismo que se compre
# Si compran menos de 5 no obtienen descuento
# si compran mas o igual de 5 y menos de 20 obtienen un 10% de descuento
# si compran mas o igual de 20 y menos de 50 obtienen un 20% de descuento
# si compran mas de o igual 50 obtienen un 30% de descuento

# Escribir una función llamada get_discount que se le pase la cantidad de productos y devuelva el descuento que le corresponde (0, 10, 20 o 30)
# Escribir otra función llamada get_final_price que se le pase el precio del producto y la cantidad de productos a comprar y devuelva el coste del producto final
# La función get_final_price debe usar la función get_discount

def get_discount(count):
    if count<5: return 0
    if count<20: return 10
    if count<50: return 20
    return 30

def get_final_price(price, count):
    return price*count*(100-get_discount(count))/100.0


def test():
    assert get_final_price(10, 4) == 40, "Should be 40"
    assert get_final_price(10, 0) == 0, "Should be 0"
    assert get_final_price(10, 5) == 45, "Should be 45"
    assert get_final_price(10, 20) == 160, "Should be 180"
    assert get_final_price(11, 22) == 193.6, "Should be 193.6"
    assert get_final_price(12, 61) == 512.4, "Should be 512.4"
    assert get_discount(100) == 30, "Should be 30"

if __name__ == "__main__":
    test()
    print("Everything passed")