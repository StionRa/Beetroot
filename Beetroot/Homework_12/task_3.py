list_one = [1, 2, 3, 4, 5]
list_two = [1, -2, 3, -4, 5]
def choose_func(x: list, func_one, func_two):
    for i in x:
        # Если встретили число ниже ноля, возвращаем результат функции func_two
        if i < 0:
            return func_two(x)
    # Если не встретили число ниже ноля, возвращаем результат функции func_one
    return func_one(x)
def square_nums(item):
    return [i ** 2 for i in item]
def remove_negatives(item):
    return list(filter(lambda it: it > 0, item))
    #return [num for num in x if num > 0]

print(choose_func(list_one, square_nums, remove_negatives))
print(choose_func(list_two, square_nums, remove_negatives))