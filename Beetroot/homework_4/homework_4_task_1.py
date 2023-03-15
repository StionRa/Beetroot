# Taking input from the user
enter_text = input('Enter your text hier: ')

# Creating formatted string
newString = "{}{}".format(enter_text[0:2], enter_text[-2:])
l = len(enter_text)

# Printing the new String
if l >= 2:
    print("Input string: " + enter_text + '\n' + "New String: " + newString)
else:
    print("Input string: " + enter_text + '\n' + "Empty String")
    #print(enter_text)