day_a = ['Monday', 'Tuesday', 'Wednesday',' Thursday',' Friday', 'Saturday', 'Sunday']
print(day_a)
day = [1, 2, 3, 4, 5, 6, 7]
day_list = [1, 'Monday', 2, 'Tuesday', 3, 'Wednesday', 4, 'Thursday', 5, 'Friday', 6, 'Saturday', 7, 'Sunday']
day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4:'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
x = dict(zip(day_a, day))
print(x)
y = dict(zip(day, day_a))
print(y)