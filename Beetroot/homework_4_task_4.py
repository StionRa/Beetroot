# Stored name in lowercase
name = "stanislav"
# input name from user
input_name = input("What is your name: ")
# converts all names to lowercase and compares
if name.lower() == input_name.lower():
    # if everything is correct, displays the names with a capital letter
    print(name.title(), 'and', input_name.title(), '= True')
else:
    # if the names do not match, outputs Fasle
    print(name.title(), 'and', input_name.title(), '= False')
