class Animal:
    def __init__(self, name):
        self.name = name

class Cat(Animal):
    def talk(self):
        print('Meow')


class Dog(Animal):
    def talk(self):
        print('woof woof')


animals = [Cat('Jorge'), Dog('Ethan')]

for animal in animals:
    animal.talk()
