# i = input("Введіть рядок: ")  # Користувач вводить рядок
#
# for x in i:  # Ітеруємося по символам рядка
#     print(ord(x), end=" ")  # Виводимо ANSII-код символу, використовуючи функцію ord()
#
#
# chr()
# import random
#
# for _ in range(5):
#     x = random.randint(1, 200)
#     conv = chr(x)
#     print(conv, end=" ")

import random

target_word = input("Введіть потрібне слово: ")  # Користувач вводить потрібне слово

generated_word = ""
count = 0
count_round = 0
while generated_word != target_word and count_round != 10:
    generated_word = ""
    for _ in range(1):
        x = random.randint(97, 122)  # Генеруємо випадкове ціле число в діапазоні від 97 до 122 (від 'a' до 'z')
        conv = chr(x)
        generated_word += conv
        count += 1

    if generated_word == target_word:
        count_round += 1
        print("Знайдено потрібне слово:", generated_word)
    if count_round == 10:
        print("Okay")
        break

print("Статистика:")
print("Загальна кількість пошуків:", count)
print("Кількість повторень:", count_round)
print("Останнє згенероване слово:", generated_word)


