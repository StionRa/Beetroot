# advanced tasks (optional):
# Find maximum from list of integers;
#     • Compute the average of tuple items;
#     • Reverse list using while loop;
#     • Copy items from one list to another;
import random
result = []
def random_num(start, stop, size):
    #result = []
    for i in range(size):
        x = random.randrange(start, stop)
        result.append(x)
    return result
print(random_num(1, 1000, 10))
def maximum_num():
    return max(result)

print('maximum from list of integers: ', maximum_num())

def average_tuple():
    return sum(result)/len(result)
print('average of tuple items: ', average_tuple())

def reverse_while():
    tluser = []
    x = len(result) - 1
    while (x >= 0):
        tluser.append(result[x])
        x = x - 1
    return tluser
print("Reverse list using while loop")
print(reverse_while())

def copy_list():
    result_copy = result[:]
    return result_copy
print(copy_list())

