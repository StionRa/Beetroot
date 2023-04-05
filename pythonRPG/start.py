import json
import os
import sys
import player

file_path = 'map_generator.json'
objects = {}
def create_new_dict(filename):
    # Check if the file exists
    if os.path.exists(filename):
        # If the file exists, check if it is empty
        if os.path.getsize(filename) == 0:
            # If the file is empty, create a new dictionary and write it to the file
            objects = [{'player_name': None, 'role': None, 'health_point': 0, 'mana_point': 0, 'player_str': 0, 'player_int': 0}]
            with open(filename, "w") as f:
                json.dump(objects, f)
            print("Created new dictionary in file:", filename)
        else:
            print("File is not empty:", filename)
    else:
        # If the file does not exist, create a new dictionary and write it to the file
        objects = [{'player_name': None, 'role': None, 'health_point': 0, 'mana_point': 0, 'player_str': 0, 'player_int': 0}]
        with open(filename, "w") as f:
            json.dump(objects, f)
        print("Created new file and dictionary:", filename)
def load_file():
    with open(file_path, 'r') as db_file_one:
        json.load(db_file_one)
def save_file():
    with open(file_path, 'w')as db_map:
            json.dump(objects, db_map)

def addObject(name, x, y, symbol):
    objects[name] = [x, y, symbol]
try:
    with open(file_path, 'r') as db_file:
        objects = json.load(db_file)
except FileNotFoundError:
    addObject('player', 6, 6, "P")

def move():
    while True:
        player = input("""
        To move around the map enter the direction or type Exit to quit game:
        'N' nord, 'S' south, 'W' west, 'E' east\n -> """).lower()
        try:
            for place in objects:
                os.system('clear')
                if player == 'n':
                    load_file()
                    if objects[place][0] == 1:
                        print('Wrong way!!!')
                    else:
                        objects[place][0] -= 1
                elif player == 's':
                    load_file()
                    if objects[place][0] == 11:
                        print('You can`t go there!!!')
                    else:
                        objects[place][0] += 1
                elif player == 'e':
                    load_file()
                    if objects[place][1] == 11:
                        print('No Way out!!!')
                    else:
                        objects[place][1] += 1
                elif player == 'w':
                    load_file()
                    if objects[place][1] == 1:
                        print("Go out there!!!")
                    else:
                        objects[place][1] -= 1
                elif player == 'q':
                    save_file()
                    db_file.close()
                    quit()
                else:
                    print('Invalid input!!')
        except:
            pass
        finally:
            save_file()
            map()
def map():
    global objects
    for x in range(11):
        line = ''
        num_x = x+1
        for y in range(11):
            num_y = y+1
            for place in objects:
                if objects[place][:2] == [num_x, num_y]:
                    line +=" " + objects[place][2] + " "
                    break
            else:
                line +=" " + '0' + " "
        print(line)









if __name__ == '__main__':
    #start_game()
    create_new_dict(file_path)
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
        objects_player = [player.open_player_file()]
        player_name = input('Please enter you Name hier: ')
        role = 'warrior'
        health_points = 5
        mana_point = 2
        player_str = 1
        player_int = 1
        objects_player_new = {'player_name': player_name, 'role': role, 'health_point': health_points, 'mana_point': mana_point, 'player_str': player_str,
                          'player_int': player_int}
        objects_player.append(objects_player_new)
        player.dump_file_player(objects_player)

        move()
    elif choise == '2':
        pass
    elif choise == '3':
        sys.exit()
    else:
        print('Wrong action!')