# day_a = ['Monday', 'Tuesday', 'Wednesday',' Thursday',' Friday', 'Saturday', 'Sunday']
# day = [1, 2, 3, 4, 5, 6, 7]
# x = dict(zip(day_a, day))
# y = dict(zip(day, day_a))
# print(day_a)
# print(x)
# print(y)
day_a = ['Monday', 'Tuesday', 'Wednesday',' Thursday',' Friday', 'Saturday', 'Sunday']
day_m = [i for i in range(1, 8)]
day_x = {day_a[i]: day_m[i] for i in range(len(day_a))}
day_rev = {day_m[i]: day_a[i] for i in range(len(day_a))}
print(day_a)
print(day_m)
print(day_x)
print(day_rev)