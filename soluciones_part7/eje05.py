# -*- coding: utf-8 -*-
# Crea una clase llamada Computer que tenga como atributos model, ram, price y state
# La clase tendrá un método llamado start que ponga el estado del ordenador a True
# La clase tendrá un método llamado off que ponga el estado del ordenador a False
# Se podrán sumar 2 ordenadores (sobrecarga del operador +), el resultado será la suma de los precios de los ordenadores

class Computer:
    def __init__(self, model, ram, price):
        self.model=model
        self.ram=ram
        self.price=price
        self.state=False
    def start(self):
        self.state=True
    def off(self):
        self.state=False
    def __add__(self, other):
        return self.price + other.price
    
def test():
    c1=Computer('HP',8,1000)
    c2=Computer('HP',4,450)
    assert c1+c2== 1450, "c1+c2 price should be 1450"
    assert c1.state== False, "by default computer c1 state should be False"
    c1.start()
    assert c1.state== True, "when start computer c1 the state should be True"

if __name__ == "__main__":
    test()
    print("Everything passed")