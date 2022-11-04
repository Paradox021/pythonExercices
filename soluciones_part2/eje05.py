# -*- coding: utf-8 -*-

# Dado número de usuarios participantes y cantidad de grupos a generar, 
# Crear función llamada create_group que devuelva 2 cosas a la vez: 
# - Número de participantes en cada grupo 
# - Personas que quedan fuera de algún grupo

def create_group(participants, groups):
    return participants//groups,participants%groups

def test():
    assert create_group(4, 2) == (2,0), "(4, 2) Should be 2,0"
    assert create_group(5, 2) == (2,1), "(5, 2) Should be 2,1"
    assert create_group(6, 3) == (2,0), "(6, 3) Should be 2,0"
    assert create_group(6, 4) == (1,2), "(6, 4) Should be 1,2"
    assert create_group(123, 5) == (24,3), "(123, 5) Should be 24,3"

if __name__ == "__main__":
    test()
    print("Everything passed")