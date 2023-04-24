import time
import timeit


# class Person:
#     # This code defines a Person class with a balance attribute that can be accessed, modified,
#     # and deleted using the property() function.
#     def __init__(self, name, balance):
#         # When a Person object is created using the __init__() method, it is initialized with a name attribute
#         # and a __balance attribute (which is hidden from direct access using the double underscore prefix).
#         self.name = name
#         self.__balance = balance
#
#     # The balance_set(), balance_get(), and balance_del() methods are defined to set, get, and delete the
#     # __balance attribute of a Person object, respectively.
#     def balance_set(self, balance):
#         self.__balance += balance
#         print('balance_set: ', self.__balance)
#
#     def balance_get(self):
#         print('balance_get: ', self.__balance)
#
#     def balance_del(self):
#         del self.__balance
#         print('balance_del: done!!!')
#     # The property() function is used to create a balance attribute that combines the balance_set(), balance_get(),
#     # and balance_del() methods. This allows the balance attribute to be accessed, modified, and deleted using dot
#     # notation (e.g. person.balance = 100, person.balance, del person.balance).
#     balance = property(balance_get, balance_set, balance_del, 'balance_doc')
#
#
# person = Person('Stas', 1000)
# person.balance = 100
# person.balance
class Person:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    @property
    def balance(self):
        return 'balance_get: ' + " " + str(self.__balance)

    @balance.setter
    def balance(self, balance):
        if balance < 0:
            raise ValueError('balance must be more as 0 $')
        self.__balance = balance
        return 'balance_set: ' + " " + str(self.__balance)

    @balance.deleter
    def balance(self):
        del self.__balance
        return 'balance_del: done!!!'


# del person.balance


class Person:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    @property
    def balance(self):
        return 'balance_get: ' + " " + str(self.__balance)

    @balance.setter
    def balance(self, balance):
        if balance < 0:
            raise ValueError('balance must be more as 0 $')
        self.__balance = balance
        return 'balance_set: ' + " " + str(self.__balance)

    @balance.deleter
    def balance(self):
        del self.__balance
        return 'balance_del: done!!!'



person = Person('Stas', 1000)
print(person.balance)
person.balance = 100
print(person.balance)
del person.balance
