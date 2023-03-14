# #7. округліть число пі (3,141592) до 3 знаків після коми.
# x = 3.141592
# print(round(x, 2))
# #Спрогнозуйте результати операцій, потім перевірте в коді.
# # 20+3*5 35
# # (20+3)*5 115
# # 6**2-50/5 26.0
# # 6**(5-2)/5 43.2
# # 4/2**3 0.5
# # 15//4%2 1
# print(20+3*5)
# print((20+3)*5)
# print(6**2-50/5)
# print(6**(5-2)/5)
# print(4/2**3)
# print(15//4%2)
#
# # 9. Виконайте перетворення типів (int, str, float), всі можливі варіанти для наступних даних. В кожному випадку постарайтесь зрозуміти результат.
# # 9
# # 12.0
# # 12.3
# # ‘12’
# # ‘23.7’
# # ‘qwerty’
# a = 9
# print(int(a), str(a), float(a), sep='-->')
# b = 12.0
# print(int(b), str(b), float(b), sep='-->')
# c = 12.3
# print(int(c), str(c), float(c), sep='-->')
# d = 23.7
# print(int(d), str(d), float(d), sep='-->')
# e = 'qwerty'
# print(int(e), str(e), float(e), sep='-->')

# # 10. Створіть змінну типу str з нульовою довжиною.
# a = ""
# print(type(a))

# 11. Створіть будь-який текст, застосувавши для нього:
#  - одинарні лапки
# - подвійні
# - потрійні (розмістіть текст в кількох рядках)

# print('Hello "Word", my """name""" is Stas')
# print("""Print
#       the
#       text hier""")

# 12. результатом print() повинні бути:
# - student’s book
# - “Kyiv”
# print('- student`s book\n- "Kyiv"')

# # 13. Продемонструйте в коді 2 варіанти використання зворотнього слешу \
# print('hello\nword\t, how are you?\'\'\'')
# # 14. Яка довжина рядка ‘qwe rty’ ? Спрогнозуйте, потім перевірте в коді.
# text = "qwe rty"
# print(len(text))
# # 15. Є змінна a=’qwerty’. Потрібно отримати наступний результат:
# # qwertyqwertyqwerty
# #  Реалізуйте мінімум 2-ма методами.
# a = "qwerty"
# print(a*3)
# print(f'{a}'*3)
# print('qwertyqwertyqwerty')
# print(f'{a}{a}{a}')
#
# 16. Є змінна beta=’qwerty’.
# Реалізуйте настуні операції, використовуючи методи для роботи з рядками:
# - визначте довжину
# - підрахуйте кількість символів ‘y’
# - отримайте слово в верхньому та нижньому регістах
# - зробіть так, щоб значення змінної beta=’QWERTY’
# - замініть ‘T’ на ‘y’
# - перевірте, чи змінна beta містить лише символи, або лише цифри
# - перевірте, чи ‘W’ входить в змінну beta
# beta = 'qwerty'
# print(len(beta))
# print(beta.count('y'))
# print(beta.upper(), beta.lower())
# l = list(beta)
# l[4], l[5] = l[5], l[4]
# print(''.join(l))
# print(beta.isdigit())
# print(beta.isalpha())
# ch = 'W'
# if ch in beta:
#     print("Character found")
# else:
#     print("Character not found")

# 17. знайдіть символи ‘q’ та ‘Q’ у змінній beta=’QWERTY’ при допомозі методів .index() та .find().
# 18. знайдіть в ‘qwertyqwerty’ символ ‘t’ при допомозі методів .find() та .rfind(). Зрозуміло, чому результати (індекси) різні ?
# 19. Отримайте з ‘qwerty’ символи ‘y’, ‘e’, ‘q’ використовуючи зворотню індексацію (індекси з від’ємним значенням).
# 20. Отримайте з ‘qwerty’ при допомозі зрізу ‘wer’:
# - використовуючи додатні індекси
# - використовуючи додатній та від’ємний індекс
# - використовуючи від’ємні індекси

# beta = 'qwerty'
# print(beta.find('q'))
# print(beta.find('r'))
# alpha = 'qwertyqwerty'
# print(alpha.find('t'))
# print(alpha.rfind('t'))
# print(beta[-1], beta[-4], beta[-6])
# print(beta[1:4])
# print(beta[1:-2])
# print(beta[-5:-2])

# 24. Маємо змінні a = ‘Zen’, b = ‘Python’, c=‘Tim’.
# З допомогою різних типів форматування (f-стрічка, format, format з індексами, %) виведіть результат:
# The Zen of Python, by Tim Peters
# 25. Є змінні PI = ‘Pi is equal to’ та pi = 3.1415.
#  Виведіть ‘Pi is equal to 3.14’, використавши форматування з заокругленням до 2 знаків після коми.
# 26. Переписати вирази для операцій над змінною з допомогою шорткатів:
# n=n+1
# n=n-1
# n=n/1
# n=n*1
# n=n**5

# a = 'Zen'
# b = 'Python'
# c = 'Tim'
# print(f'The {a} of {b}, by {c} Peters')
# print('The {0} of {1}, by {2} Peters'.format('Zen', 'Python', 'Tim'))
# print('The {0} of {1}, by {2} Peters'.format(a, b, c))
#
# PI = 'Pi is equal to'
# pi = 3.1415
# print(PI, round(pi, 2))
# n = 5
# n +=1
# n -=1
# n /=1
# n *=1
# n **=1
# print(n)
#
# 1. Прорахуйте результат, потім перевірте в коді:
# (True and not True and True)  False
# (True and True or True)       True
#  (False or True or not False) True
# (False and True and False)    False

# 2. Який оператор (and, or) неявно використовується при множинному порівнянні ?
# Розберіть на прикладах, перевірте в коді:
# (2<3<4<5)     True and
#  (4>3<6<9)    True and
# Створіть код (з використанням if) який буде виводити назву дня тижня в залежності від значення змінної day_name, яка може приймати значення 1..7.
first_day = 'Monday'
second_day = 'Tuesday'
the_third_day = 'Wednesday'
fourth_day = 'Thursday'
fifth_day = 'Friday'
sixth_day = 'Saturday'
seventh_day = 'Sunday'
present_day = int(input('What day of the week is it, enter an integer: '))
if present_day >= 7:
    if present_day == 1:
        print(first_day)
    elif present_day == 2:
        print(second_day)
    elif present_day == 3:
        print(the_third_day)
    elif present_day == 4:
        print(fourth_day)
    elif present_day == 5:
        print(fifth_day)
    elif present_day == 6:
        print(sixth_day)
    elif present_day == 7:
        print(seventh_day)
    else:
        print("What a beautiful day")
else:
    print("Must be a Integer digit only!!")