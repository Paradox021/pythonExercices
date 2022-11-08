
# Herencia multiple

class Animal:
    def __init__(self, name):
        self.name=name
    # Para que sea privado se usa los dos guiones bajo
    def __eat(self):
        pass
    @staticmethod
    def max_time_live():
        return 400

class Npc:
    def __init__(self, hp):
        self.hp=hp

class Duck(Animal, Npc):
    def __init__(self, name, hp):
        super().__init__(name)

lucas = Duck('lucas',100)
print(lucas.name)

# class Duck(Animal, Npc):
#   def __init__(self, name, hp):
#        Animal.__init__(self, name)
#        Npc.__init__(self, hp)

class First(object):
    def __init__(self):
        super(First, self).__init__()
        print("first")

class Second(object):
    def __init__(self):
        super(Second, self).__init__()
        print("second")

class Third(First, Second):
    def __init__(self):
        super(Third, self).__init__()
        print("third")

Third()