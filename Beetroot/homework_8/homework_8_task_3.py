def make_operation(operator, *numbers):
    total = 0
    if operator == '+':
        for num in numbers:
            total += num
        return total
    if operator == '-':
        total = numbers[0]  # The first number
        for num in numbers[1:]:  # index 1 to the last number
            total -= num
        return total
    if operator == '*':
        total = numbers[0]
        for num in numbers[1:]:
            total *= num
        return total

print(make_operation('+', 7, 7, 2) )
print(make_operation('-', 5, 5, -10, -20))
print(make_operation('*', 7, 6) )