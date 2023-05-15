# # # Задачки на урок: (реалізація через рекурсію !!!)
# # #  Задача 1.
# # #  Визначте функцію print_to, яка приймає одне натуральне число n і роздруковує на екрані послідовність цілих чисел
# # #  від 1 до n до включно. Кожне число необхідно виводити в окремому рядку.
# #
# # def print_to(n):
# #     if n > 1:
# #         print_to(n - 1)
# #     print(n)
# #
# #
# # print(print_to(5))
# #
# #
# # def print_reverse(n, lst):
# #     if n == 0:
# #         return
# #     print(lst[n - 1], end=' ')
# #     print_reverse(n - 1, lst)
# #
# #
# #
# # n = 3
# # lst = [1, 2, 3]
# # print_reverse(n, lst)
# #
# #
# # n = 5
# # lst = [5, 9, 3, 2, 7]
# # print_reverse(n, lst)
#
#
# # Напишіть функцію, яка приймає на вхід список із цілих чисел і повертає суму елементів переданого списку.
#
# def sum_list(lst):
#     if not lst:
#         return 0
#     else:
#         return lst[0] + sum_list(lst[1:])
#
#
# lst = [1, 2, 3, 4, 5]
# print(sum_list(lst))

def flatten(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten(item))  # рекурсивно додаємо його елементи до flat_list
        else:
            flat_list.append(item)  # якщо елемент не є списком, то додаємо його в flat_list
    return flat_list


lst1 = [1, [2, 3, [4]], 5]
print(flatten(lst1))

lst2 = [1, [2, 3], [[2], 5], 6]
print(flatten(lst2))

lst3 = [[[[9]], [1, 2], [[8]]]]
print(flatten(lst3))
