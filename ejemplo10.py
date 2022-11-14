
#docStrings
#docTest
def add(n1, n2):
    '''Este metodo suma 2 números'''
    '''
    >>>add(5,2)
    7
    '''
    return n1+n2

print(add(4,2))

print('el nombre del método es:',add.__name__)
print('lo que hace el método es:',add.__doc__)

#python -m doctest -v ejemplo10.py