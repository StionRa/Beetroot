# Option 1 - creating a list of numbers from 1 to 100 in 1 step
my_list = [*range(1, 101, 1)]
# creating new empty list
my_new_list = []
# run a loop with my_list to check how many numbers in the list are divisible by 7 and not divisible by 5
for i in my_list:
    if (i%7==0) and (i%5!=0):
        # enter values into a list my_new_list
        my_new_list.append(str(i))
# and display them to the user
print(','.join(my_new_list))

# # Option 2 - creating empty list my_new_list
# my_new_list=[]
# # creating range between 1 and 100
# for x in range(1, 100):
#     # checking which numbers in this range are divisible by 7 and not divisible by 5
#     if (x%7==0) and (x%5!=0):
#         # enter values into a list my_new_list
#         my_new_list.append(str(x))
#         # and display them to the user
# print (','.join(my_new_list))

