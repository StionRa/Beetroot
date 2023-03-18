# some_string = {}
# string_text = input("Enter some string 'text': ")
# list_of_words = string_text.split()
# for word in list_of_words:
#     some_string[word] = some_string.get(word, 0) + 1
# print('Word Frequency')
# for key in some_string.keys():
#     print(key, some_string[key])
# print(some_string)


# stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}
# prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}
# #  результирующий словарь
# total_price = {}
# # пробегаем по ключам словаря
# for key in stock and prices:
#     try:
#         # умножаем значения
#         total_price[key] = stock[key] * prices[key]
#     # если ключа еще нет - создаем
#     except KeyError:
#         total_price[key] = stock[key]
# # Выводим результат
# print(total_price)
#
# comprehension_list = [(i , i**2) for i in range (11)]
# print(comprehension_list)
import random
day_a = ['Monday', 'Tuesday', 'Wednesday',' Thursday',' Friday', 'Saturday', 'Sunday']
day = [1, 2, 3, 4, 5, 6, 7]
day_list = [1, 'Monday', 2, 'Tuesday', 3, 'Wednesday', 4, 'Thursday', 5, 'Friday', 6, 'Saturday', 7, 'Sunday']
print(type(day_list))
day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4:'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
print(type(day_dict))
x = dict(zip(day_a, day))
print(x)
y = dict(zip(day, day_a))
print(y)