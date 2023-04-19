class Animal:
    def talk(self):
        pass


class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def talk(self):
        print("woof woof")


class Cat(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def talk(self):
        print("meow")


def make_animal_talk(animal: Animal):
    animal.talk()


dog = Dog("Fluffy", 2.5)
cat = Cat("Kitty", 4)
for animal in (dog, cat):
    make_animal_talk(animal)
    animal.info()
