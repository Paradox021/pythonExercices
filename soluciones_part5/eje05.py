# -*- coding: utf-8 -*-
# En tu granja tienes una lista de animales, 
# y quieres saber cuantos patos tienes de color negro y cuyo id empieza por G

animals = [
    {'id':'G37429F', 'type': 'duck', 'color': 'black'},
    {'id':'KH39FUH', 'type': 'duck', 'color': 'black'},
    {'id':'JD387DH', 'type': 'cow', 'color': 'black'},
    {'id':'KDH38FD', 'type': 'duck', 'color': 'white'},
    {'id':'SJ20DJH', 'type': 'cow', 'color': 'white'},
    {'id':'HSHJF83', 'type': 'donky', 'color': 'brown'},
    {'id':'GH555UH', 'type': 'duck', 'color': 'black'},
]
def count_ducks(list):
    cont=0
    for animal in list:
        if animal['type']=='duck' and animal['color']== 'black' and animal['id'].startswith('G'):
            cont+=1
    return cont

def test():
    assert count_ducks(animals) == 2, "You hava 2 ducks"

if __name__ == "__main__":
    test()
    print("Everything passed")