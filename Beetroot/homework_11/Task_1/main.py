import json
def create_file():
    with open('myfile.txt', 'w') as file:
        file.write('Hello file world!\n')

def open_file():
    with open('myfile.txt', 'r') as file:
        text = file.read()
        print(text)

create_file()
open_file()
