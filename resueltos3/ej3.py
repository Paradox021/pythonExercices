# Dada una lista llamada teachers, haz un duplicado de la misma en otra lista llamada employees

teachers = ['Juan', 'Pedro', 'Ana', 'Maria', 'Luis']
employees = teachers.copy()

def test():
    teachers[0]='Peter'
    assert employees[0] == 'Juan', "The first employee should be Juan"



if __name__ == "__main__":
    test()
    print("Everything passed")