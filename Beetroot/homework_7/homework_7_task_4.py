# day_a = ['Monday', 'Tuesday', 'Wednesday',' Thursday',' Friday', 'Saturday', 'Sunday']
# day = [1, 2, 3, 4, 5, 6, 7]
# x = dict(zip(day_a, day))
# y = dict(zip(day, day_a))
# print(day_a)
# print(x)
# print(y)
day_a = ['Monday', 'Tuesday', 'Wednesday',' Thursday',' Friday', 'Saturday', 'Sunday']
day_x = {day_a[i]: i+1 for i in range(len(day_a))}
day_rev = {i+1: day_a[i] for i in range(len(day_a))}
print(day_a)
print(day_x)
print(day_rev)