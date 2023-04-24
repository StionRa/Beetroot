# Створити клас клієнта банку, який приймає атрибути:
# ПІБ
# баланс рахунку (захищений атрибут)
# Реалізувати методи (звичайні, не property), які б дозволили:
# отримувати баланс
# присвоювати баланс
# видаляти атрибут баланс
# Створити екземпляр класу, відпрацювати всі методи.

# class BankAccount:
#     def __init__(self, fname, lname, birthday, debit, credit):
#         self.fname = fname
#         self.lname = lname
#         self.birthday = birthday
#         self.__debit = debit
#         self.__credit = credit
#     def get_debit(self):
#         return self.__debit
#
#     def set_debit(self, amount):
#         if amount < 0:
#             raise ValueError('Debit amount must be positive')
#         self.__debit = amount
#
#     def del_debit(self):
#         del self.__debit
#
#     bank_account = property(get_debit, set_debit, del_debit, "hi")
#
#
# person = BankAccount("Zelinskyi", "Stas", "09/08/1983", 100, 350)
# person.set_debit(234)
# print(person.get_debit())
# person.del_debit()
# print(person)

# Створити клас Авто, приймає атрибути:
# Марка авто
# Модель авто
# Пробіг
# Вартість (приватний атрибут)
# Реалізувати методи (для атрибуту „вартість“) через синтаксис (my_property = property(getx, setx, delx, "I'm the 'x' property.")
# Створити екземпляр класу,
# відпрацювати всі методи,
# викликати стрічку документації.

# class Auto:
#     def __init__(self, mark, model, km, price):
#         self.mark = mark
#         self.model = model
#         self.km = km
#         self.__price = price
#
#     def price_get(self):
#         return self.__price
#
#     def price_set(self, value):
#         self.__price = value
#
#     def price_del(self):
#         del self.__price
#
#     my_property = property(price_get, price_set, price_del, f"I'm the x property.")
#
#
# auto = Auto("Volvo", "XC60", 12000, 26000)
# auto.my_property = 27000
# print(Auto.my_property.__doc__)

# Скопіювати рішення для задачі 2, переробити таким чином, щоб для геттера, сеттера та делітера використовувалось одне і те ж ім“я.

# class Auto:
#     def __init__(self, mark, model, km, price):
#         self.mark = mark
#         self.model = model
#         self.km = km
#         self.__price = price
#
#     @property
#     def price(self):
#         'Hello am doc'
#         return self.__price
#
#     @price.setter
#     def price(self, value):
#         self.__price = value
#
#     @price.deleter
#     def price(self):
#         del self.__price
#
#
#
# auto = Auto("Volvo", "XC60", 12000, 26000)
# auto.price = 27000
# print(auto.price)
# print(Auto.price.__doc__)

#
# Ваш клас з задачі 1 почав використовуватись програмістами, що працюють в банку. В процесі роботи виявилось,
# що в ПІБ записуються не коректні дані. Прогнозувалось, що ПІБ – це стрінг, в якому знаходяться 3 слова,
# розділені пробілами, кожне - з великої букви. На практиці – туди інколи скидається різна «каша», типу «Петренко
# В.В», «кум Петро», «Бульба С. – голова колгоспу» і т.д. і т.п. Ваша задача – зробити з ПІБ властивість (property),
# з відповідними операціями (гетер, сетер, делітер), для сетера виконати необхідні перевірки, інакше – викидати
# виключення з описом помилки.

# class BankAccount:
#     def __init__(self, fname, birthday, debit, credit):
#         self.fname = fname
#         self.birthday = birthday
#         self.__debit = debit
#         self.__credit = credit
#     @property
#     def full_name(self):
#         return f"{self.fname}"
#     @full_name.setter
#     def full_name(self, value):
#         words = value.split()
#         if len(words) != 3:
#             raise ValueError("Full name should contain 3 words")
#         if not all(word.istitle() for word in words):
#             raise ValueError("Not Titel")
#         self.fname = value
#
# person = BankAccount("Zelinskyi Stanislav Olegovich", "09/08/1983", 100, 100)
#
# #print(person.full_name)
# person.full_name = 'Stas Zil Ole'
# print(person.full_name)


# class Calculator:
#     @staticmethod
#     def add(*args):
#         if len(args) < 1 or len(args) > 10:
#             raise ValueError("Expected between 1 to 10 digits")
#         total = sum(args)
#         return total
#
# print(Calculator.add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# # create class generator
# a = (i for i in range(10))
# print(a, type(a))
# # create class list
# a = [i for i in range(10)]
# print(a, type(a))
#
# def gen(i):
#     for x in range(i):
#         yield x
# s = gen(10)
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))

class I:
    def __init__(self, object):
        self.index = 0
        self.end = len(object) - 1
        self.object = object

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > self.end:
            raise StopIteration("Stop Iteration")
        result = self.object[self.index]
        self.index += 1
        return result

i = I([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
enumerate