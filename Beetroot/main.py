# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def dispaly_person_info(self):
#         print(f"Person: {self.name}, {self.age}")
#
# class Company:
#     def __init__(self, company_name, location):
#
#         self.company_name = company_name
#         self.location = location
#     def dispaly_company_info(self):
#         print(f"Company: {self.company_name}, {self.location}")
#
# class Employee(Person, Company):
#     def __init__(self, name, age, company_name, location):
#         Person.__init__(self, name, age)
#         Company.__init__(self, company_name, location)
#
# pers = Employee('Stas', 24, "BBC", "Kiev")
#
# pers.dispaly_company_info()
# pers.dispaly_person_info()


class Class_1:
    def print_name(self):
        return Class_1.__name__

class Class_2(Class_1):
    def print_name(self):
        return Class_2.__name__

class Class_7(Class_1):
    def print_name(self):
        return Class_7.__name__
class Class_6(Class_7):
    def print_name(self):
        return Class_6.__name__
class Class_5(Class_6):
    def print_name(self):
        return Class_3.__name__

class Class_4(Class_5):
    def print_name(self):
        return Class_4.__name__

class Class_3(Class_4):
    def print_name(self):
        return Class_3.__name__



class Class_8(Class_2, Class_3, Class_6):
    def print_name(self):
        return Class_8.__name__


a = Class_8()
print(a.print_name())
print(Class_8.mro())