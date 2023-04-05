#Write a Python program to construct the following pattern, using a while loop
n = 8
for i in range(1, n // 2 + 2):
    print('*' * i, sep='\n')
for i in range(n // 2, 0, -1):
    print('*' * i)

# #Write a python program, which sums all digits in a python string.
# #Examples, input - ‘1234’, output - 10
#
# sum_digits = input("enter your number: ")
# sum_digit = 0
# for x in sum_digits:
#     if x.isdigit() == True:
#         z = int(x)
#         sum_digit = sum_digit + z
# print(sum_digit)

# # Write a Python program that accepts a string and calculate the number of digits, letters and other characters in the input string
#
# sum_text = input("enter your number: ")
# print(len(sum_text))

