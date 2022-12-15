# -*- coding: utf-8 -*-
import math

# Crea una función llamada collision, se le pasarán la velocidad de dos objetos (km/h) y la distancia que los separan (km)
# esta devolverá cuanto tiempo (en horas) tardarán en encontrarse
# La formula que tienes que usar es tiempo(s) = distancia(m) / (velocidad1 (m/s) +velocidad2 (m/s))

def collision(v1,v2,d):
    return d/(v1+v2)

def test():
    assert math.isclose(collision(5,4,50), 5.55555555), "Should be 5.55555"


if __name__ == "__main__":
    test()
    print("Everything passed")