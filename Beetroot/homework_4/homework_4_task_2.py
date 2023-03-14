# Taking input from the user
phone_number = input("Enter the phone number: ")
length = len(phone_number)
# check the number for length and numbers
if length == 10 and phone_number.isdigit():
    # if everything is correct output Valid
    print("Valid Phone Number")
    # if everything is wrong, output Invalid
else :
    print("Invalid Phone Number")