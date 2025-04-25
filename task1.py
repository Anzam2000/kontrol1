
class Animal:
    def make_sound(self):
        pass
class Dog(Animal):
    def make_sound(self):
        print('Собака лает')
class Cat(Animal):
    def make_sound(self):
        print('Кошка мяукает')
cat = Cat()
dog = Dog()
cat.make_sound()
dog.make_sound()
