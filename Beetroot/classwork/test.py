import json

 def greate_new_user(First_Name, Last_Name, Telephone_nummer, City_State):
    with open('user.json', 'w') as file_object:
        my_dict = {'First_Name' : 'Stas', 'Last_Name' : 'Zelinskyi', 'telephone_nummer' : 730608069, 'City_State' : 'Odessa'}
        json.dump(my_dict, file_object)