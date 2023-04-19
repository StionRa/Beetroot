import json
import os

filename = "data_person.json"


def create_file():
    # Check if the file exists
    if os.path.exists(filename):
        # If the file exists, check if it is empty
        if os.path.getsize(filename) == 0:
            # If the file is empty, create a new dictionary and write it to the file
            data = {"person": []}
            with open(filename, "w") as f:
                json.dump(data, f)
            print("Created new dictionary in file:", filename)
        else:
            print("File is not empty:", filename)
    else:
        # If the file does not exist, create a new dictionary and write it to the file
        data = {"person": []}
        with open(filename, "w") as f:
            json.dump(data, f)
        print("Created new file and dictionary:", filename)


def open_file():
    # Check if the file exists
    if not os.path.exists(filename):
        print("File does not exist:", filename)
        return []

    # Read the file and return the data as a list of dictionaries
    with open(filename, "r") as f:
        data_new = json.load(f)
        return data_new["person"]


def save_file(name_file):
    with open(filename, 'w') as f:
        json.dump(name_file, f)


def append_to_file(new_data):
    # Read the current data from the file
    current_data = open_file()
    # Append the new data to the current data
    current_data.append(new_data)
    # Write the updated data back to the file
    with open(filename, "w") as f:
        json.dump({"person": current_data}, f)


def new_person():
    print("Create new person:"
          "Input you data")
    choise = input('''
    To create new person:
    1. new Student:
    2. New Teacher''')
    if choise == "1":
        print('''
        Enter your parametrs:''')

        first_name = input("Your First name:")

        last_name = input("Your Last name:")
        birthday = input("Your birthday:")
        email = input("your email adres:")
        new_data = {"students": [{"first_name": first_name, "last_name": last_name, "birthday": birthday, "email": email}]}
        append_to_file(new_data)
    elif choise == "2":
        pass
    else:
        print("Wrong Value")


def info_person():
    with open(filename, 'r') as f:
        person = json.load(f)
        for pers in person['person']:
            return f'{pers["first_name"]} {pers["last_name"]} - {pers["birthday"]}, {pers["email"]}'


def all_person():
    with open(filename, "r") as f:
        data = json.load(f)

    people = data["person"]
    for person in people:
        print(f"Name: {person['first_name']} {person['last_name']}")
        print(f"Birthday: {person['birthday']}")
        print(f"Email: {person['email']}\n")


def find_user(user_name):
    with open(filename, 'r') as f:
        data = json.load(f)

    user_dict = None
    for person in data['person']:
        if person['first_name'] == user_name:
            user_dict = person
            break
    if user_dict:
        print(f"Name: {user_dict['first_name']} {user_dict['last_name']}")
    else:
        print(f"{user_name} not found in base.")


if __name__ == "__main__":
    # new_person()
    find_user('Stas')
