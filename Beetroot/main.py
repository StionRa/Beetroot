# day_name=int(input(" Введите день недели: "))
#
# if day_name == 1:
#     print('Monday')
# elif day_name == 2:
#     print('Tuesday')
# elif day_name == 3:
#     print('Wensday')
# elif day_name == 4:
#     print('Thusday')
# elif day_name == 5:
#     print(' Friday')
# elif day_name == 6:
#     print('Suturday')
# elif day_name ==7:
#     print('Sunday')
# else:
#     print('Error')
#
# print(day_name)


print(__import__("calendar").day_name[int(input())])