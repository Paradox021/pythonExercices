# -*- coding: utf-8 -*-
# Almacena en una variable person de tipo diccionario los datos basicos de una persona
# name, surname, age, dni, country, hobies, skills, is_married
# tambien se guardará los points(puntos) obtenidos en los 3 torneos que ha participado (usando un diccionario)


person = {
    "name":"a",
    "surname":"a",
    "age":20,
    "dni":"123456789",
    "country":"a",
    "hobbies":["a","b"],
    "skills":["a","b","c"],
    "is_married":False,
    "points":{ "1":1, "2":2, "3":3}
}

def test():
    assert type(person) is dict, "person should be a dictionary"
    assert 'name' in person, "person should have a name"
    assert 'surname' in person, "person should have a surname"
    assert 'age' in person, "person should have a age"
    assert 'dni' in person, "person should have a dni"
    assert 'country' in person, "person should have a country"
    assert 'hobbies' in person, "person should have a hobbies"
    assert 'skills' in person, "person should have a skills"
    assert 'is_married' in person, "person should have a is_married"
    assert 'points' in person, "person should have a points"
    assert type(person['name']) is str, "name should have a string value"
    assert type(person['surname']) is str, "surname should have a string value"
    assert type(person['age']) is int, "age should have a namber value"
    assert type(person['dni']) is str, "dni should have a string value"
    assert type(person['country']) is str, "country should have a string value"
    assert type(person['hobbies']) is list, "hobbies should have a list value"
    assert type(person['skills']) is list, "skills should have a list value"
    assert type(person['is_married']) is bool, "is_married should have a boolean value"
    assert type(person['points']) is dict, "points should have a dictionary value"
    assert len(person['points']) == 3, "points should have 3 elements"


if __name__ == "__main__":
    test()
    print("Everything passed")