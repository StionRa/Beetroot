import json
import os

file_path = 'player_stats.json'
objects_player = {'player_name': None, 'role': None, 'health_point': 0, 'mana_point': 0, 'player_str': 0, 'player_int': 0}
def create_new_dict(filename):
    # Check if the file exists
    if os.path.exists(filename):
        # If the file exists, check if it is empty
        if os.path.getsize(filename) == 0:
            # If the file is empty, create a new dictionary and write it to the file
            objects_player = {'player_name': None, 'role': None, 'health_point': 0, 'mana_point': 0, 'player_str': 0, 'player_int': 0}
            with open(filename, "w") as f:
                json.dump(objects_player, f)
            print("Created new dictionary in file:", filename)
        else:
            print("File is not empty:", filename)
    else:
        # If the file does not exist, create a new dictionary and write it to the file
        objects_player = {'player_name': None, 'role': None, 'health_point': 0, 'mana_point': 0, 'player_str': 0, 'player_int': 0}
        with open(filename, "w") as f:
            json.dump(objects_player, f)
        print("Created new file and dictionary:", filename)
def open_file_player():
    with open(file_path, 'r') as file_read:
        json.load(file_read)
def dump_file_player(objects_player):
    with open(file_path, 'w') as file_dump:
        json.dump(objects_player, file_dump)
def player_statistic():
    pass
def open_player_file():
    pass