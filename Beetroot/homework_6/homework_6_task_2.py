# import random module
import random
# # Introductory text prompting you to press enter to start or type exit to quit
# text = 'Press "enter" to start, or type "exit" to exit: '
# # Starting while loop
# while True:
#     message = input(text)
#     # if the user has entered exit quit the program
#     if message == 'exit':
#         break
#     else:
#         # output custom text if present or empty string
#         print(message)
#     # Get random int in range 0 - 100 only 10 numbers in list_a and list_b
#     list_a = random.sample(range(0, 100), 10)
#     list_b = random.sample(range(0, 100), 10)
#     # compare the results in list_a and list_b and output the common integers
#     common_list = list(set(list_a).intersection(list_b))
#     print(list_a)
#     print(list_b)
#     print("Common integers in the list:", common_list)
#     # exit program
#     break

# while True:
#     num_a = [i for i in random.sample(range(-11, 11) ,10)]
#     num_b = [j for j in random.sample(range(-11, 11) ,10)]
#     num_c = []
#     for i in num_a:
#         for j in num_b:
#             if i == j:
#                 num_c.append(i)
#     print(num_c)
#     break
# print(num_a)
# print(num_b)
num1 = set()
num2 = set()
large = 10
while len(num1) < large:
     num_gen = random.randint(1, 40)
     if num_gen not in num1:
          num1.add(num_gen)
while len(num2)< large:
     num_gen = random.randint(1, 40)
     if num_gen not in num2:
          num2.add(num_gen)
while True:
     #com_int = [i for i in num1 and num2 if i in num1 and num2]
     com_int = []
     for i in num1:
          if i in num2:
               if i not in com_int:
                    com_int.append(i)

     #com_int = [i for i in num_test_1 and num_test_2 if i in num_test_1 and num_test_2]
     break


print(num1, len(num1))
print(num2, len(num2))
print(com_int)