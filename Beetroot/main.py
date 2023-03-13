# # day_name=int(input(" Введите день недели: "))
# #
# # if day_name == 1:
# #     print('Monday')
# # elif day_name == 2:
# #     print('Tuesday')
# # elif day_name == 3:
# #     print('Wensday')
# # elif day_name == 4:
# #     print('Thusday')
# # elif day_name == 5:
# #     print(' Friday')
# # elif day_name == 6:
# #     print('Suturday')
# # elif day_name ==7:
# #     print('Sunday')
# # else:
# #     print('Error')
# #
# # print(day_name)
#
#
# print(__import__("calendar").day_name[int(input())])

import random

user_name: str = input("Please insert name: ")
print("Greeting, " + str(user_name))
print("Let`s play rock, papper, scissors")
player = input("Choise rock, papper or scrissors by typing r, p or s: ")
if player == 'r' or player == 'p' or player == 's':
    computer = random.randint(1, 3)
    # 1 == r
    # 2 == p
    # 3 == s
    if (computer == 1 and player == 'r' or computer == 2 and player == 'p' or
        computer == 3 and player == "s"):
        print("It is draw")
    elif (computer == 1 and player == "p" or computer == 2 and player == "s" or
        computer == 3 and player == "r"):
        print("Congratulations, You Win!!!")
    else:
        print("You Lost!")
else:
    print("Your input was wrong format, no game for you")