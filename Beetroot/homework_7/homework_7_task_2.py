stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}
prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}
#  результирующий словарь
total_price = {}
# пробегаем по ключам словаря
for key in stock and prices:
    try:
        # умножаем значения
        total_price[key] = stock[key] * prices[key]
    # если ключа еще нет - создаем
    except KeyError:
        total_price[key] = stock[key]
# Выводим результат
print(total_price)