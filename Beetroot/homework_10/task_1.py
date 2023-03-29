def oops():
    raise IndexError
def catch():
    try:
        oops()
    except IndexError:
        print('Caught Index Error')
catch()
#але не має відповіді на питання для задачі 1 (не зарах.):
#'What happens if you change oops to raise KeyError instead of IndexError?'

# Here's what's going to happen:

# Traceback (most recent call last):
#   File "/home/stanislavus/PycharmProjects/Beetroot/homework_10/task_1.py", line 8, in <module>
#     catch()
#   File "/home/stanislavus/PycharmProjects/Beetroot/homework_10/task_1.py", line 5, in catch
#     oops()
#   File "/home/stanislavus/PycharmProjects/Beetroot/homework_10/task_1.py", line 2, in oops
#     raise KeyError
# KeyError

#The catch function will not catch the Index Error, and the oops function itself will throw a key error
