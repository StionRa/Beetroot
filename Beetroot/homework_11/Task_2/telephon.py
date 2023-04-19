# Extend Phonebook application v.0.0.1 test
import json
import os
import sys
# Define the name of the JSON file
FILE_NAME = 'telephone_book_1.json'
#FILE_NAME = sys.argv[1]
# Load existing data from JSON file or initialize an empty dictionary
try:
    with open(FILE_NAME, 'r') as f:
        telephone_book = json.load(f)
except FileNotFoundError:
    print(f"File {FILE_NAME} not found!", file=sys.stderr)
    telephone_book = []
class MyException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

# def read_data():
#     with open(FILE_NAME, 'r') as f:
#         json.read(telephone_book, f)
def add_entry():

    while True:
        first_name = input('please, input your First Name: ').lower()
        if (first_name == ''):
            print('First Name can`t be leer')
            continue
        else:
            break
    while True:
        last_name = input('please, input your Last Name: ').lower()
        if (last_name == ''):
            print('Last name can`t be leer')
            continue
        else:
            break
    while True:
        country = input('please, input your City or Country: ').lower()
        if (country == ''):
            print('Country can`t be leer')
            continue
        else:
            break
    while True:
        telephone = input('please, input your Telephone: ')
        if (telephone == ''):
            print('Telephone can`t be leer')
            continue
        elif not telephone.isdigit():
            print('Must be digit')
            continue
        else:
            break
    entry = {
        'first_name': first_name,
        'last_name': last_name,
        'country': country,
        'telephone': telephone
    }
    telephone_book.append(entry)
    save_data()
    print(f'{first_name.capitalize()} {last_name.capitalize()}, has been added to the telephone book.')


# Define a function to search for an entry in the telephone book
def search_entry_name():
    name = input("Enter name to search for: ")
    for entry in telephone_book:
        if name in (entry['first_name'], entry['last_name']):
            print(f"{entry['first_name']} {entry['last_name']}: {entry['country']} - {entry['telephone']}")
            return
    print(f"{name} not found in the telephone book.")
    #raise MyException (f"{name} not found in the telephone book.")
def search_entry_last():
    name = input("Enter Last name to search for: ")
    for entry in telephone_book:
        if name in (entry['first_name'], entry['last_name']):
            print(f"{entry['first_name']} {entry['last_name']}: {entry['country']} - {entry['telephone']}")
            return
    print(f"{name} not found in the telephone book.")
    #raise MyException (f"{name} not found in the telephone book.")
def search_entry_full():
    name = input("Enter Full name to search for: ").lower().split(' ')
    for entry in telephone_book:
        if len(name) != 2:
            print('must be First name and Last name')
            return
        elif name[0] and name[1] in (entry['first_name'], entry['last_name']):
            print(f"{entry['first_name']} {entry['last_name']}: {entry['country']} - {entry['telephone']}")
            return
        else:
            continue
    print(f"{name} not found in the telephone book.")
    #raise MyException (f"{name} not found in the telephone book.")
def search_entry_telephone():
    name = input("Enter Telephone to search for: ")
    for entry in telephone_book:
        if name in (entry['first_name'], entry['telephone']):
            print(f"{entry['first_name']} {entry['last_name']}: {entry['country']} - {entry['telephone']}")
            return
    print(f"{name} not found in the telephone book.")
    #raise MyException (f"{name} not found in the telephone book.")
#Fix search for all members who live in the same city. Now showing the first one in the database
def search_entry_city():
    name = input("Enter City to search for: ")
    for entry in telephone_book:
        if name in (entry['first_name'], entry['country']):
            print(f"{entry['first_name']} {entry['last_name']}: {entry['country']} - {entry['telephone']}")
            return
    print(f"{name} not found in the telephone book.")
    #raise MyException (f"{name} not found in the telephone book.")
# Define a function to delete an entry from the telephone book
def delete_entry():
    name = input("Enter Telephone to delete contact: ")
    for entry in telephone_book:
        if name in (entry['telephone']):
            telephone_book.remove(entry)
            save_data()
            print(f"{entry['first_name']} {entry['last_name']} has been deleted from the telephone book.")
            return
    print(f"{name} not found in the telephone book.")
    #raise MyException (f"{name} not found in the telephone book.")
def update_entry():
    name = input("Enter telephone to update contact: ")
    for entry in telephone_book:
        if name in (entry['first_name'], entry['telephone']):
            telephone_book.remove(entry)
            first_name = input('please, input your First Name: ').lower()
            last_name = input('please, input your Last Name: ').lower()
            country = input('please, input your City or Country: ').lower()
            telephone = input('please, input your Telephone: ')
            entry = {
                'first_name': first_name,
                'last_name': last_name,
                'country': country,
                'telephone': telephone
            }
            telephone_book.append(entry)
            save_data()
            print(f"{first_name} {last_name} has been update to the telephone book.")
            return
    print(f"{name} not found in the telephone book.")
# Define a function to save the data to the JSON file
def save_data():
    with open(FILE_NAME, 'w') as f:
        json.dump(telephone_book, f)
# Main loop of the program
def start():
    while True:
        print("\nTelephone Book")
        print("==============")
        print("1. Add Entry")
        print("2. Search Entry")
        print("3. Delete Entry")
        print("4. Update Entry")
        print("5. Quit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_entry()
        elif choice == '2':
            print("\nSearch by:")
            print("==============")
            print("1. Search by first name")
            print("2. Search by last name")
            print("3. Search by full name")
            print("4. Search by telephone number")
            print("5. Search by city or state")
            print("6. Quit")
            print("==============")
            choice = input("Enter your choice: ")
            if choice == '1':
                search_entry_name()
            elif choice == '2':
                search_entry_last()
            elif choice == '3':
                search_entry_full()
            elif choice == '4':
                search_entry_telephone()
            elif choice == '5':
                search_entry_city()
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please try again.")
                # raise MyException ("Invalid choice. Please try again.")
        elif choice == '3':
            delete_entry()
        elif choice == '4':
            update_entry()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")
            #raise MyException ("Invalid choice. Please try again.")
if __name__ == '__main__':
    start()