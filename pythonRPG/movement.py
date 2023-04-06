
player_map_icon = ['P', 6, 6]
def map():
    for x in range(11):
        line = ''
        num_x = x + 1
        for y in range(11):
            num_y = y + 1
            if player_map_icon[-2:] == [num_x, num_y]:
                line += " " + player_map_icon[0] + " "
            else:
                line += " " + '0' + " "
        print(line)


def move():
    while True:
        try:
            map()
            print(player_map_icon)
            choise = input("Nord - Up, South - Down, West - Left, East - Rigth: ").lower()
            if choise == 'n':
                if player_map_icon[1] == 1:
                    print("You can`t go this way!")
                else:
                    player_map_icon[1] -= 1
            elif choise == 's':
                if player_map_icon[1] == 11:
                    print("You can`t go this way!")
                else:
                    player_map_icon[1] += 1
            elif choise == 'w':
                if player_map_icon[2] == 1:
                    print("You can`t go this way!")
                else:
                    player_map_icon[2] -= 1
            elif choise == 'e':
                if player_map_icon[2] == 11:
                    print("You can`t go this way!")
                else:
                    player_map_icon[2] += 1
            else:
                print('Invalid input!!')
        except:
            pass

move()
print(player_map_icon)