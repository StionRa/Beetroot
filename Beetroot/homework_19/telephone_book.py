# Extend Phonebook application v.0.0.1 test
import json
import sys


class Phonebook:
    def __init__(self, filename='telephone_book.json'):
        self.filename = filename
        self.load_data()

    def load_data(self):
        try:
            with open(self.filename, 'r') as f:
                self.telephone_book = json.load(f)
        except FileNotFoundError:
            print(f"File {self.filename} not found!", file=sys.stderr)
            self.telephone_book = []

    def save_data(self):
        with open(self.filename, 'w') as f:
            json.dump(self.telephone_book, f)

    def add_entry(self):
        while True:
            first_name = input('please, input your First Name: ').title()
            if first_name == '':
                print('First Name can`t be leer')
                continue
            elif first_name.isdigit():
                print('Must be a character')
                continue
            else:
                break
        while True:
            last_name = input('please, input your Last Name: ').title()
            if last_name == '':
                print('Last name can`t be leer')
                continue
            elif last_name.isdigit():
                print('Must be a character')
                continue
            else:
                break
        while True:
            country = input('please, input your City or Country: ')
            if country == '':
                print('Country can`t be leer')
                continue
            elif country.isdigit():
                print('Must be a character')
                continue
            else:
                break
        while True:
            telephone = input('please, input your Telephone: ')
            if telephone == '':
                print('Telephone can`t be leer')
                continue
            elif not telephone.isdigit():
                print('Must be digit')
                continue
            else:
                break
        entry = {
            'first_name': first_name.title(),
            'last_name': last_name.title(),
            'country': country,
            'telephone': telephone
        }
        self.telephone_book.append(entry)
        self.save_data()
        print(f'{first_name.title()} {last_name.title()}, has been added to the telephone book.')

    def search_entry_name(self):
        name = input("Enter name to search for: ").capitalize()
        for entry in self.telephone_book:
            if name in (entry['first_name'], entry['last_name']):
                print(f"{entry['first_name']} {entry['last_name']}: {entry['country']} - {entry['telephone']}")
                return
        print(f"{name} not found in the telephone book.")

    def search_entry_last(self):
        name = input("Enter Last name to search for: ").capitalize()
        for entry in self.telephone_book:
            if name in (entry['first_name'], entry['last_name']):
                print(f"{entry['first_name']} {entry['last_name']}: {entry['country']} - {entry['telephone']}")
                return
        print(f"{name} not found in the telephone book.")

    def search_entry_full(self):
        name = input("Enter Full name to search for: ").capitalize().split(' ')
        for entry in self.telephone_book:
            if len(name) != 2:
                print('must be First name and Last name')
                return
            elif name[0] and name[1] in (entry['first_name'], entry['last_name']):
                print(f"{entry['first_name']} {entry['last_name']}: {entry['country']} - {entry['telephone']}")
                return
            else:
                continue
        print(f"{name} not found in the telephone book.")

    def search_entry_telephone(self):
        name = input("Enter Telephone to search for: ")
        for entry in self.telephone_book:
            if name in (entry['first_name'], entry['telephone']):
                print(
                    f"{entry['first_name']} {entry['last_name']}: {entry['country']} - {entry['telephone']}")
                return
        print(f"{name} not found in the telephone book.")

    # Fix search for all members who live in the same city. Now showing the first one in the database
    def search_entry_city(self):
        name = input("Enter City to search for: ").capitalize()
        for entry in self.telephone_book:
            if name in (entry['first_name'], entry['country']):
                print(f"{entry['first_name']} {entry['last_name']}: {entry['country']} - {entry['telephone']}")
                return
        print(f"{name} not found in the telephone book.")
        # raise MyException (f"{name} not found in the telephone book.")

    # Define a function to delete an entry from the telephone book
    def delete_entry(self):
        name = input("Enter Telephone to delete contact: ").capitalize()
        for entry in self.telephone_book:
            if name in (entry['telephone']):
                self.telephone_book.remove(entry)
                self.save_data()
                print(f"{entry['first_name']} {entry['last_name']} has been deleted from the telephone book.")
                return
        print(f"{name} not found in the telephone book.")
        # raise MyException (f"{name} not found in the telephone book.")

    def update_entry(self):
        name = input("Enter telephone to update contact: ").capitalize()
        for entry in self.telephone_book:
            if name in (entry['first_name'], entry['telephone']):
                self.telephone_book.remove(entry)
                while True:
                    first_name = input('please, input your First Name: ').title()
                    if first_name == '':
                        print('First Name can`t be leer')
                        continue
                    elif first_name.isdigit():
                        print('Must be a character')
                        continue
                    else:
                        break
                while True:
                    last_name = input('please, input your Last Name: ').title()
                    if last_name == '':
                        print('Last name can`t be leer')
                        continue
                    elif last_name.isdigit():
                        print('Must be a character')
                        continue
                    else:
                        break
                while True:
                    country = input('please, input your City or Country: ')
                    if country == '':
                        print('Country can`t be leer')
                        continue
                    elif country.isdigit():
                        print('Must be a character')
                        continue
                    else:
                        break
                while True:
                    telephone = input('please, input your Telephone: ')
                    if telephone == '':
                        print('Telephone can`t be leer')
                        continue
                    elif not telephone.isdigit():
                        print('Must be digit')
                        continue
                    else:
                        break
                entry = {
                    'first_name': first_name.title(),
                    'last_name': last_name.title(),
                    'country': country,
                    'telephone': telephone
                }
                self.telephone_book.append(entry)
                self.save_data()
                print(f"{first_name} {last_name} has been update to the telephone book.")
                return
        print(f"{name} not found in the telephone book.")


# def start():
#     phonebook = Phonebook("my_telephone_book.json")
#     while True:
#         print("\nTelephone Book")
#         print("==============")
#         print("1. Add Entry")
#         print("2. Search Entry")
#         print("3. Delete Entry")
#         print("4. Update Entry")
#         print("5. Quit")
#         choice = input("Enter your choice: ")
#         if choice == '1':
#             Phonebook.add_entry(phonebook)
#         elif choice == '2':
#             print("\nSearch by:")
#             print("==============")
#             print("1. Search by first name")
#             print("2. Search by last name")
#             print("3. Search by full name")
#             print("4. Search by telephone number")
#             print("5. Search by city or state")
#             print("6. Quit")
#             print("==============")
#             choice = input("Enter your choice: ")
#             if choice == '1':
#                 Phonebook.search_entry_name(phonebook)
#             elif choice == '2':
#                 Phonebook.search_entry_last(phonebook)
#             elif choice == '3':
#                 Phonebook.search_entry_full(phonebook)
#             elif choice == '4':
#                 Phonebook.search_entry_telephone(phonebook)
#             elif choice == '5':
#                 Phonebook.search_entry_city(phonebook)
#             elif choice == '6':
#                 break
#             else:
#                 print("Invalid choice. Please try again.")
#                 # raise MyException ("Invalid choice. Please try again.")
#         elif choice == '3':
#             Phonebook.delete_entry(phonebook)
#         elif choice == '4':
#             Phonebook.update_entry(phonebook)
#         elif choice == '5':
#             break
#         else:
#             print("Invalid choice. Please try again.")
#             # raise MyException ("Invalid choice. Please try again.")
#
#
# if __name__ == '__main__':
#     start()
