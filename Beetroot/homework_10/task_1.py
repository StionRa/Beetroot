def oops():
    raise IndexError
def catch():
    try:
        oops()
    except IndexError:
        print('Caught Index Error')
catch()