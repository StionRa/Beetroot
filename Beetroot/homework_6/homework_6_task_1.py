
#    VARIANT 1
import random # import random module
#
# while True:
#     user_digit = input("Enter the maximum random number that can be generated between 1 and 15: ")
#     # asking the user to enter digits
#     # Get random int in range 1 - 15 only 10 numbers
#     n = random.sample(range(1, 15), 10)
#     print("RANDOM", n) # show generated numbers
#     print("Max", max(n)) # show max number
#     print("Min", min(n)) # show min number
#     print("Length", len(n)) # show length of numbers
#     if str(max(n)) == user_digit: #check the number entered by the user and the maximum number generated by the program
#         print("You guessed the number!!") #If they match, the user is congratulated and the program ends with a break.
#         break
# #If the numbers don't match, we go back to the beginning of the while loop
#
#
# #     VARIANT 2
#
# import random  # import random module
# n = random.sample(range(1, 15), 10)
# n.sort()
# print(n)
# print("Найбольшее число: ", n[-1])

while True:
    num = random.sample(range(-100, 100), 10)
    print(num)
    max = num[0]
    for n in num:
        if n > max: max = n
        print(max)
        continue
    else:
        break