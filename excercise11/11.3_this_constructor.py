#called its own cunstructor explicitly...
class Animal:

    def __init__(self):
        print("Parent class")

class Mammal(Animal):

    def __init__(self):
        print("Child class")
    def this_method(self):
        Mammal() #called its own cunstructor with argument explicitly...

m = Mammal()
m.this_method()