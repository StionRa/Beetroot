# Усіма улюблена програма "hello world". Створіть функцію з ім'ям say_hello_world , яка приймає на вхід ім'я людини у вигляді рядка і друкує фразу "{name} говорить hello world!"
# def say_hello_world(name):
#     return name + " say hello world!"
# print(say_hello_world('Stas'))
from typing import Tuple


# Напишіть функцію check_password, яка перевіряє переданий їй пароль на складність і друкує на екран результат перевірки.
# Складним паролем вважатиметься комбінація символів, у якій :
# Є хоча б 3 цифри
# Є хоча б одна велика літера
# Є хоча б один символ із наступного набору "!@#$%%*"
# Загальна довжина не менше 10 символів
# Якщо пароль пройшов усі перевірки, функція повинна вивести на екран фразу "Perfect password", в іншому випадку - "Easy peasy"

# def check_password(password):
#     # password = input('Введите пароль:')
#     digits = '1234567890'
#     upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     lower_letters = 'abcdefghijklmnopqrstuvwxyz'
#     symbols = '!@#$%^&*()-+'
#     acceptable = digits + upper_letters + lower_letters + symbols
#
#     passwd = set(password)
#     if any(char not in acceptable for char in passwd):
#         print('Ошибка. Запрещенный спецсимвол')
#     else:
#         recommendations = []
#         if len(password) < 12:
#             recommendations.append(f'увеличить число символов - {12 - len(password)}')
#         for what, message in ((digits, 'цифру'),
#                               (symbols, 'спецсимвол'),
#                               (upper_letters, 'заглавную букву'),
#                               (lower_letters, 'строчную букву')):
#             if all(char not in what for char in passwd):
#                 recommendations.append(f'добавить 1 {message}')
#
#         if recommendations:
#             print("Слабый пароль. Рекомендации:", ", ".join(recommendations))
#         else:
#             print('Сильный пароль.')
#
# print(check_password('12345zxcvbASDFG!@#$$'))
# # # tests
# # for test in ("qwety", "Qwert_Y", "Q123wer123tY", "A^B@C*D", "@PowerRangers123@"):
# #     print("Password:", test)
# #     check_password(test)
# #     print()


# 3. Ваше завдання написати функцію get_domain_name, яка приймає рядок url, витягує з нього доменне ім'я і повертає його як рядок
# get_domain_name("http://google.com") => "google"
# get_domain_name("http://google.co.jp") => "google"
# get_domain_name("www.xakep.ru") => "xakep"
# get_domain_name("https://youtube.com") => "youtube"
# get_domain_name("https://www.asos.com") => "asos"
# get_domain_name("http://www.lenovo.com") => "lenovo"
# URL може починатися з протоколів http:// https:// або з www. URL, що починаються з протоколів http:// https://, можуть також містити www.


def get_domain_name(name):
    domain = name.replace('http://', '')
    domain_2 = domain.replace('https://', '')
    dom = domain_2.replace('www.', '')
    na_dom = dom.split('.')[0]
    return na_dom
print(get_domain_name("xakep.ru"))
print(get_domain_name("www.xakep.ru"))
print(get_domain_name("http://google.com"))
print(get_domain_name('http://www.lenovo.com'))
print(get_domain_name('http://google.co.jp'))
print(get_domain_name("https://www.asos.com"))
print(get_domain_name("https://youtube.com"))
print(get_domain_name("https://docs-python.ru/tutorial/ispolzovanie-tekstovyh-strok-python/preobrazovanija-manipuljatsii-strokami/"))