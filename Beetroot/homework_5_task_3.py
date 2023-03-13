import random # Import random module
test_list = str(input("Text: ")) # input text from user
i = 0
while i < 5: #generating while loops
    print(''.join(random.choice(test_list) for i in range(5))) # generating new word from user word in range 5 digits
    if i == 5: # cycle step check
        break
    i += 1