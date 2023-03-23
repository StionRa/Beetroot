# 4. Напишіть функцію count_args, яка приймає довільну кількість аргументів. Ця функція повинна повертати кількість переданих їй на вхід аргументів
# count_args(1, 2, 3) => 3
# count_args(1, 3) => 2
# count_args(2) => 1
# count_args() => 0
# def count_args(*args):
#     num = len(args)
#     return num
# print(count_args(1, 2, 3, 4, 5))
# print(count_args('qwqwr', 'qwrqwr', 123, 'qw'))

# 5. Напишіть функцію info_kwargs, яка приймає довільну кількість іменованих аргументів.
# Функція info_kwargs повинна роздрукувати іменовані аргументи в кожному новому рядку у вигляді пари <Ключ> = <Значення>, причому ключі повинні слідувати в алфавітному порядку. Приклад роботи дивіться нижче
# info_kwargs(first_name="John", last_name="Doe", age=33)
# """" цей виклик друкує такі рядки
# age = 33
# first_name = John
# last_name = Doe
# """
# def info_kwargs(**kwargs):
#     for key, value in sorted(kwargs.items()):
#         print('%s = %s' % (key, value))
#
#
# info_kwargs(first_name="John", last_name="Doe", age=33)

# 6. Задача на область видимості:
# Напишіть
# функцію, яка приймає ім'я та вік водія.
# Функція повинна роздрукувати на екран
# висновок, чи може даний водій керувати
# транспортом і визначати вона повинна
# це за віком водія: він має бути більшим
# або дорівнювати MIN_DRIVING_AGE
# Якщо
# водій може керувати, виведіть фразу
# "<name> може водити>
# " , в іншому разі "<name> ще рано
# сідати за кермо"
# MIN_DRIVING_AGE
# = 18
# allowed_driving('tim',
# 17) # виведе "tim ще рано сідати за кермо"
# allowed_driving('bob',
# 18) # виведе "bob може водити"

# def min_drive_age(name, age):
#     if age < 18:
#         print(name, 'ще рано сідати за кермо')
#     else:
#         print(name, 'може водити')
#
# min_drive_age('Stas', 17)

# Створіть функцію, яка має 4 параметри: a,b,c,d, а потім виводить їх через print.
#  Передайте аргументи в функцію наступними способами:
#  - як позиційні
# - як іменовані, по порядку,
# - як іменовані, в довільному порядку
# - 2 аргументи як позиційні, 2 – як іменовані
# - 2 аргументи як іменовані, 2 – як позиційні

def complex(a, b, c, d):
    print(a, b, c, d)
complex(1, 2, 3, 4)

def complex_two(a = 1, b = 2, c = 3, d = 4):
    print(a, b, c, d)
complex_two()

def complex_tree(a = 10, b = 15, c = 21, d = 13):
    print(c, a, d, b)
complex_tree()

def complex_four(a, b, c = 21, d = 98):
    print(b, a, c, d)
complex_four(1, 2)

def complex_five(a , b, c = 73, d = 666):
    print(d, c, a, b)
complex_five(3, 4)