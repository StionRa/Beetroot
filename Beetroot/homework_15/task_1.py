# School
#
# Make a class structure in python representing people at school. Make a base class called Person,
# a class called Student, and another one called Teacher. Try to find as many methods and attributes as you can
# which belong to different classes, and keep in mind which are common and which are not. For example, the name
# should be a Person attribute, while salary should only be available to the teacher.

class Person:
    total_people = 0
    total_students = 0
    total_teachers = 0

    def __init__(self, name, age, birthday):
        self.name = name
        self.age = age
        self.birthday = birthday
        Person.total_people += 1


class Student(Person):
    def __init__(self, name, age, birthday, graduationyear, curse):
        super().__init__(name, age, birthday)
        self.graduationyear = graduationyear
        self.curse = curse
        Person.total_students += 1

    def display_students(self):
        print(f"Name: {self.name}, Year: {self.graduationyear}, Curs: {self.curse}")
    def welcome(self):
        print("Welcome", self.name, "to the coure of", self.curse, self.graduationyear)


class Teacher(Person):
    def __init__(self, name, age, birthday, work, lect):
        super().__init__(name, age, birthday)
        self.work = work
        self.lect = lect
        Person.total_teachers += 1

    def display_teachers(self):
        print(f'Name: {self.name}, Work: {self.work}, Lect: {self.lect}')


people = Student('Stas', 39, '09.08.1983', 2023, "Python")
people1 = Teacher("Alex", 21, "09.09.2010", "Lector", "Development")
people2 = Teacher("Qwerty", 27, "12 Aug 2011", "Mentor", "English")
people.display_students()
people2.display_teachers()
print(f"total: {Person.total_people}, students: {Person.total_students}, teachers: {Person.total_teachers}")
people.welcome()
