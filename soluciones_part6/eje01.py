# -*- coding: utf-8 -*-
# Crea una clase llamada Product, que tenga los atributos name, price, dto y category
# La clase tendrá un método llamado get_price_final que devuelva el precio final del producto (con su descuento aplicado)
# La clase tendrá un método llamado __str__ que devuelva el nombre y el precio del producto (separados por un guión)
# Crea un objeto llamado product_to_send de la clase Product con los siguientes valores:
# - name: Pantalon
# - price: 100
# - dto: 10
# - category: ropa


class Product:
    def __init__(self, name, price, dto, category):
        self.name=name
        self.price=price
        self.dto=dto
        self.category=category
    def get_price_final(self):
        return self.price - self.price * self.dto / 100

    def __str__(self):
        return self.name+'-'+str(self.price)


product_to_send = Product('Pantalon', 100, 10, 'ropa')
def test():
    #assert type(Product).__name__ == 'classobj', "Product should be a class"
    assert isinstance(product_to_send,Product), "product_to_send should be a Product"
    assert product_to_send.name == 'Pantalon', "product_to_send.name should be 'Pantalon'"
    assert product_to_send.price == 100, "product_to_send.price should be 100"
    assert product_to_send.dto == 10, "product_to_send.dto should be 10"
    assert product_to_send.category == 'ropa', "product_to_send.category should be 'ropa'"
    assert product_to_send.get_price_final() == 90, "product_to_send.get_price_final() should be 90"
    assert product_to_send.__str__() == 'Pantalon-100', "product_to_send.__str__() should be 'Pantalon-100'"

if __name__ == "__main__":
    test()
    print("Everything passed")