import json
import os
import sys
import player as db_player
db_player.create_new_dict(db_player.file_path)
pos = db_player.open_position_player()
objects = []
objects.append(pos)
def move():
    while True:
        player = input("""
        To move around the map enter the direction or type Exit to quit game:
        'N' nord, 'S' south, 'W' west, 'E' east\n -> """).lower()
        try:
            for place in objects:
                os.system('clear')
                if player == 'n':
                    db_player.open_file_player()
                    if objects[place][0] == 1:
                        print('Wrong way!!!')
                    else:
                        objects[place][0] -= 1
                elif player == 's':
                    db_player.open_file_player()
                    if objects[place][0] == 11:
                        print('You can`t go there!!!')
                    else:
                        objects[place][0] += 1
                elif player == 'e':
                    db_player.open_file_player()
                    if objects[place][1] == 11:
                        print('No Way out!!!')
                    else:
                        objects[place][1] += 1
                elif player == 'w':
                    db_player.open_position_player()
                    if objects[place][1] == 1:
                        print("Go out there!!!")
                    else:
                        objects[place][1] -= 1
                elif player == 'q':
                    #db_player.dump_file_player_all()
                    quit()
                else:
                    print('Invalid input!!')
        except:
            pass
        finally:
            #db_player.dump_file_player_all()
            map()
def map():
    global objects
    for x in range(11):
        line = ''
        num_x = x+1
        for y in range(11):
            num_y = y+1
            for place in objects:
                if objects[place][-2:] == [num_x, num_y]:
                    line +=" " + objects[place][2] + " "
                    break
            else:
                line +=" " + '0' + " "
        print(line)









if __name__ == '__main__':
    db_player.create_new_dict(db_player.file_path)
    print('Welkomme in to Text Role Play Game')
    print('''
    This game is under constraction.
    But now you can test it. Just come in!!
    ''')
    choise = input("""
    Make choise, what you want to do:
    1. enter a game:
    2. load save game:
    3. exit
    """)
    if choise == '1':
        objects_player = [db_player.open_file_player()]
        player_name = input('Please enter you Name hier: ')
        role = 'warrior'
        health_points = 5
        mana_point = 2
        player_str = 1
        player_int = 1
        objects_player_new = {"player_name": player_name, "role": role, "health_point": health_points, "mana_point": mana_point, "player_str": player_str, "player_int": player_int, "position_x": 6, "position_y": 6}
        objects_player.append(objects_player_new)
        db_player.dump_file_player(objects_player)

        move()
    elif choise == '2':
        pass
    elif choise == '3':
        sys.exit()
    else:
        print('Wrong action!')