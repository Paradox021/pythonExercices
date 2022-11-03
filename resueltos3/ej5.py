# función llamada insert_my_name que añada tu nombre a una lista
# Si la lista tiene un número impar de elementos, añade tu nombre en el medio
# Si la lista tiene un número par de elementos, añade tu nombre al final

def insert_my_name(list, yourName):
    # your code here
    if len(list)%2==0:
        list.append(yourName)
        return
    list.insert(round(len(list)/2),yourName)
    print(list)

list2 = ['Juan','Pedro']
insert_my_name( list2, 'Ana')
print("----" , list2 )


def test():
    
    list = ['Juan']
    insert_my_name( list, 'Ana') 
    assert list == ['Juan','Ana'], "should be  ['Juan','Ana']"

    list = ['Juan','Pedro']
    insert_my_name( list, 'Ana') 
    assert list == ['Juan','Ana','Pedro'], "should be ['Juan','Ana','Pedro']"

    list = []
    insert_my_name( list, 'Ana') 
    assert list == ['Ana'], "should be  ['Ana']"

if __name__ == "__main__":
    test()
    print("Everything passed")