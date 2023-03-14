import random # import random module
enter_text = input("Enter your text, number or value: ") # asking the user to enter text or digits to generate
enter_text = list(enter_text) # translate the text entered by the user into a list
i = 0 # specify the initial step for the cycle while
while i < 5: # we run the cycle while indicating to check which step it is, if it is less than 5, then we execute the cycle
    random.shuffle(enter_text) # we generate unique letter combinations from the text entered by the user
    print(''.join(enter_text)) # output using the print function the resulting word once per line without spaces
    if i == 5: # check the loop, if the loop step is 5, perform a break on the next line
        break
    i += 1 # if the loop step is less than 5, add +1 to "i" and return to the beginning of the loop