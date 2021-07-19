name =""
class Animal:

    def __init__(self, name):
        print("A " + name + " is an animal")

class Mammal(Animal):

    def __init__(self, name):
        print("A " + name + " is a mammal")
    def this_method(self):
        Mammal(name) #called its own cunstructor explicitly...

m = Mammal("Dog")
m.this_method()