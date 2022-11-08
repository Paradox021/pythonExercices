# -*- coding: utf-8 -*-
# Crea una clase Chicken que herede de Bird.
# Crea una clase Duck que herede de Bird.
# Los atributos que tendrán que tener serán:
# - name
# - age
# - colors
# - weight
# - can_fly
# - can_swim

# La clase Chicken se construirá con los atributos name, age, colors y weight. Por defecto no puede volar o nadar
# La clase Duck se construirá con los atributos name, age, colors y weight. Por defecto puede volar y nadar

# Crea 2 objetos:
# - un pato llamado lucas_duck, de 88 años, de color amarillo y negro, y que pesa 30 kilos
# - una gallina llamado calimero, de 1 años, de color amarillo y que pesa 3 kilos


class 

class 


class 


lucas_duck =
calimero = 

def test():
    assert type(Bird).__name__ == 'classobj', "Bird should be a class"
    assert type(Duck).__name__ == 'classobj', "Duck should be a class"
    assert type(Chicken).__name__ == 'classobj', "Chicken should be a class"
    assert isinstance(lucas_duck,Duck), "lucas_duck should be a Duck"
    assert isinstance(lucas_duck,Bird), "lucas_duck should be a Bird"
    assert isinstance(calimero,Chicken), "calimero should be a Chicken"
    assert isinstance(calimero,Bird), "calimero should be a Bird"
    assert lucas_duck.name.lower() == 'lucas', "lucas_duck.name should be 'Lucas'"
    assert lucas_duck.age == 88, "lucas_duck.age should be 88"
    assert lucas_duck.colors == ['yellow', 'black'], "lucas_duck.colors should be ['yellow', 'black']"
    assert lucas_duck.weight == 30, "lucas_duck.weight should be 30"
    assert lucas_duck.can_fly == True, "lucas_duck.can_fly should be True"
    assert lucas_duck.can_swim == True, "lucas_duck.can_swim should be True"
    assert calimero.name.lower() == 'calimero', "calimero.name should be 'Calimero'"
    assert calimero.age == 1, "calimero.age should be 1"
    assert calimero.colors == ['yellow'], "calimero.colors should be ['yellow']"
    assert calimero.weight == 3, "calimero.weight should be 3"
    assert calimero.can_fly == False, "calimero.can_fly should be False"
    assert calimero.can_swim == False, "calimero.can_swim should be False"




if __name__ == "__main__":
    test()
    print("Everything passed")