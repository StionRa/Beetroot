# Doggy age
#
# Create a class Dog with class attribute `age_factor` equals to 7. Make __init__()
# which takes values for a dog’s age. Then create a method `human_age` which returns
# the dog’s age in human equivalent.

class Dog:
    age_factor = 7

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.convert_age = Dog.age_factor * age

    def human_age(self):
        print("Hello", self.name, "your dog age is", str(self.convert_age), "Congratulate!!!")


human = Dog("Stas", 39)

Dog.human_age(human)
