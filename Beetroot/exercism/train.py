def exchange_money(budget , exchange_rate):
    return budget/exchange_rate
print(exchange_money(127.5, 1.2))

def get_change(budget, exchanging_value):
    return budget - exchanging_value
print(get_change(127.5, 120))

def get_value_of_bills(denomination, number_of_bills):
    return denomination * number_of_bills
print(get_value_of_bills(5, 128))

def get_number_of_bills(budget, denomination):
    return  budget // denomination
print(get_number_of_bills(127.5, 5))

def get_leftover_of_bills(budget, denomination):
    return budget%denomination
print(get_leftover_of_bills(127.5, 20))

def exchangeable_value(budget, exchange_rate, spread, denomination):
    return ((budget / (exchange_rate * (1 + spread / 100))) // denomination) * denomination
print(exchangeable_value(127.25, 1.20, 10, 5))