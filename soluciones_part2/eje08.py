# -*- coding: utf-8 -*-

# Elaborar una función llamada get_points() que permita especificar el número de
# partidos ganados, perdidos y empatados por tu equipo en el torneo.
# Se debe de mostrar su puntaje total.
# Teniendo en cuenta que por cada partido ganado obtendrá 3 puntos, empatado 1 punto y perdido 0 puntos.
# Si los 3 parametros no son de tipo entero se devolverá None

###### pon aquí tu código
def get_points(wins,lost,tie):
    if not type(wins) == int or not type(lost) == int or not type(tie) == int:
        return None
    return wins*3 + tie



def test():
    assert get_points(3,4,2) == 11, "Should be 11"
    assert get_points(3,4,'h') == None, "Should be 0"
    assert get_points(True,4,5) == None, "Should be 0"



if __name__ == "__main__":
    test()
    print("Everything passed")