# # import random
# #
# # def r1():
# #     return random.randint(0, 10)
# #
# # def r2():
# #     return random.randint(0, 100)
# #
# # def r3():
# #     return random.randint(0, 300)
# #
# # def main(func1, func2, func3):
# #     def even_func():
# #         while True:
# #             result = random.choice([func1(), func2(), func3()])
# #             if result % 2 == 0:
# #                 return result
# #     return even_func
# #
# # # Example usage
# # even_func = main(r1, r2, r3)
# # print(even_func)
# # print(r1(), r2(), r3())
# #
# # #Змініть задачу 1 таким чином, щоб функція main() приймала на вхід довільну кількість функцій.
# #
# # def r1():
# #     return random.randint(0, 10)
# #
# # def r2():
# #     return random.randint(0, 100)
# #
# # def r3():
# #     return random.randint(0, 300)
# #
# # def main(*funcs):
# #     def even_func():
# #         while True:
# #             result = random.choice([func() for func in funcs])
# #             if result % 2 == 0:
# #                 return result
# #     return even_func
# #
# # # Example usage
# # even_func = main(r1, r2, r3)
# # print(even_func)
# # print(r1(), r2(), r3())
#
# # A simple calculator.
# # Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter (to keep things simple let it only be ‘+’, ‘-’ or ‘*’) and an arbitrary number of arguments (only numbers) as the second parameter. Then return the sum or product of all the numbers in the arbitrary parameter. For example:
# # the call make_operation(‘+’, 7, 7, 2) should return 16
# # the call make_operation(‘-’, 5, 5, -10, -20) should return 30
# # the call make_operation(‘*’, 7, 6) should return 42
# # def make_operation(operator, *args):
# #     if operator == '+':
# #         result = sum(args)
# #     elif operator == '-':
# #         result = args[0] - sum(args[1:])
# #     elif operator == '*':
# #         result = 1
# #         for arg in args:
# #             result *= arg
# # #     else:
# # #         raise ValueError('Invalid operator')
# # #     return result
# # # print(make_operation('*', 7, 6))
# # def add(*args):
# #         return sum(args)
# #
# # def subtract(a, b):
# #     return a - b
# #
# # def multiply(a, b):
# #     return a * b
# #
# # operations = {
# #     '+': add,
# #     '-': subtract,
# #     '*': multiply,
# # }
# #
# # def make_operation(operator, *args):
# #     if operator not in operations:
# #         raise ValueError(f"Invalid operator '{operator}'")
# #     op_func = operations[operator]
# #     return op_func(*args)
# #
# # print(make_operation('+', 7, 7, 2))  # Output: 16
# # print(make_operation('-', 5, 5, -10, -20))  # Output: 30
# # print(make_operation('*', 7, 6))  # Output: 42
#
#
#
# # Нехай в нас є функція func(), яка повертає кортеж 10-ти цілих чисел в діапазоні 0 до 100.
# #  Зробіть декоратор з використанням функції map(). Задекорована функція повинна повертати список чисел, кратний 2 (реалізувати при допомозі lambda).
# import random
# # def multiple_of_two(func):
# #     def wrapper():
# #         result = func()
# #         return list(map(lambda x: x if x % 2==0 else None, result))
# #     return wrapper
# #
# # # Example usage
# # @multiple_of_two
# # def func():
# #     return tuple(random.randint(0, 100) for _ in range(10))
# # print(func())
# #
# # #Зробіть декоратор для функції func() з задачі 4, який відфільтровує значення, кратні 3. Використати функцію filter() та lambda.
# # def filter_multiples_of_three(func):
# #     def wrapper():
# #         return list(filter(lambda x: x % 3 != 0, func()))
# #     return wrapper
# #
# # @filter_multiples_of_three
# # def func():
# #     return tuple(random.randint(0, 100) for i in range(10))
# # print(func())
# # print(func())   # Output: [97, 64, 82, 62, 22]
# #
# #Зробіть декоратор для функції func() з задачі 4, який запускає дану функцію 2 рази, а потім повертає результат при допомозі zip (об“єднує отримані в результаті запусків кортежі)
# # def run_twice_and_zip(func):
# #     def wrapper():
# #         results = []
# #         for i in range(2):
# #             results.append(func())
# #         return list(zip(*results))
# #     return wrapper
# # import random
# #
# # @run_twice_and_zip
# # def func():
# #     return tuple(random.randint(0, 100) for i in range(10))
# #
# # print(func())
#
# # from functools import reduce
# #
# # def apply_reduce(func):
# #     def wrapper():
# #         return list(reduce(lambda x: ))
# #     return wrapper
# # import random
# #
# # @apply_reduce
# # def func():
# #     return tuple(random.randint(0, 100) for i in range(10))
# #
# # print(func())
# # #
# from functools import reduce
#
# # def map_decorator(func):
# #     def wrapper(*args, **kwargs):
# #         return list(map(lambda x: x if x % 2 == 0 else '', func(*args, **kwargs)))
# #     return wrapper
# #
# #
# # @map_decorator
# # def func():
# #     return tuple(random.randint(0, 100) for i in range(10))
# #
# # result = func()
# # print(result)
#
# def decorator_with_param(param):
#     def map_decorator(func):
#         def wrapper(*args, **kwargs):
#             return list(map(lambda x: x if x % param == 0 else None, func(*args, **kwargs)))
#         return wrapper
#
#     def filter_decorator(func):
#         def wrapper(*args, **kwargs):
#             return list(filter(lambda x: x % param != 0, func(*args, **kwargs)))
#         return wrapper
#
#     def zip_decorator(func):
#         def wrapper(*args, **kwargs):
#             results = []
#             for _ in range(param):
#                 results.append(func(*args, **kwargs))
#             return list(zip(*results))
#         return wrapper
#
#     def reduce_decorator(func):
#         def wrapper(*args, **kwargs):
#             return reduce(lambda x, y: x * y, func(*args, **kwargs))
#         return wrapper
#
#     if param == 2:
#         return map_decorator
#     elif param % 3 == 0:
#         return filter_decorator
#     elif param == 4:
#         return zip_decorator
#     elif param == 5:
#         return reduce_decorator
#     else:
#         raise ValueError("Invalid parameter value")
#
# # Usage example
# @decorator_with_param(2)
# def func():
#     return (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
#
# result = func()
# print(result)
