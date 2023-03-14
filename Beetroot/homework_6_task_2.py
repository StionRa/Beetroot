# import random module
import random
# Introductory text prompting you to press enter to start or type exit to quit
text = 'Press "enter" to start, or type "exit" to exit: '
# Starting while loop
while True:
    message = input(text)
    # if the user has entered exit quit the program
    if message == 'exit':
        break
    else:
        # output custom text if present or empty string
        print(message)
    # Get random int in range 0 - 100 only 10 numbers in list_a and list_b
    list_a = random.sample(range(0, 100), 10)
    list_b = random.sample(range(0, 100), 10)
    # compare the results in list_a and list_b and output the common integers
    common_list = list(set(list_a).intersection(list_b))
    print(list_a)
    print(list_b)
    print("Common integers in the list:", common_list)
    # exit program
    break
