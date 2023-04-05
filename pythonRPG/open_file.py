import io
import json
import os
from start import objects
file_path = 'map_generator.json'
map_gen = objects
def startupCheck():
    try:
        with open(file_path, 'r') as db_map:
            map_gen = json.load(db_map)
            print(f'File {file_path} exist')
    except FileNotFoundError:
        print(f'File {file_path} not found, creating a new one.')
        map_gen = []
        with open(file_path, 'w') as db_map:
            json.dump(file_path, db_map)
def load_file():
    try:
        with open(file_path, 'r') as db_file:
            json.load(db_file)
    except FileNotFoundError:
        print(f'File {file_path} not found.')
def save_file():
    with open(file_path, 'w')as db_map:
            json.dump(map_gen, db_map)