# -*- coding: utf-8 -*-
# Dado estos 4 elementos, una tupla, una lista, un diccionario y un set.
# Añade un elemento 0 al principio (si puedes) de cada una de las colecciones
# Borra el elemento del final (si puedes) de cada una de las colecciones
# NOTA: es importante que los punteros a la memoria de cada una de las colecciones no cambien
# es decir, que no se cree una nueva colección, sino que se modifique la existente

my_tupla=(1,2,3,4,5)
my_list=[1,2,3,4,5]
my_dictionary = {"uno":1,"dos":2,"tres":3,"cuatro":4,"cinco":5}
my_set={1,2,3,4,5}



id_my_tupla = id(my_tupla)
id_my_list = id(my_list)
id_my_dictionary = id(my_dictionary)
id_my_set = id(my_set)



# añadir un elemento al principio de my_list
my_list.insert(0, 0)

# añadir un elemento al principio de my_tupla
# no se puede

# añadir un elemento al principio de my_dictionary
# no se puede

# añadir un elemento al principio de my_set
# no se puede

# eliminar el ultimo elemento de la tupla
# no se puede

# eliminar el ultimo elemento de la lista
my_list.pop()

# eliminar el ultimo elemento del diccionario
#my_dictionary.popitem()

# eliminar el ultimo elemento del set
#my_set.remove(0)




def test():
    assert id_my_tupla == id(my_tupla), "No change the pointer to the memory of tupla"
    assert id_my_list == id(my_list), "No change the pointer to the memory of list"
    assert id_my_dictionary == id(my_dictionary), "No change the pointer to the memory of dictionary"
    assert id_my_set == id(my_set), "No change the pointer to the memory of set"
    
    assert type(my_tupla) == tuple, "Should be a tuple"
    assert type(my_list) == list, "Should be a list"
    assert type(my_dictionary) == dict, "Should be a dictionary"
    assert type(my_set) == set, "Should be a set"

    assert len(my_tupla) == 5, "Should be 5 elements en tupla"
    assert len(my_list) == 5, "Should be 5 elements in list"
    assert len(my_dictionary) == 5, "Should be 5 elements"
    assert len(my_set) == 5, "Should be 5 elements"
    
    assert my_tupla[0] == 1, "1 Should be first elements of tupla"
    assert my_list[0] == 0, "0 Should be first elements o list"
    assert 'cero' not in my_dictionary, "'cero': 0 not Should be in dictionary"
    assert 0 not in my_set, "0 not Should be in set"



if __name__ == "__main__":
    test()
    print("Everything passed")