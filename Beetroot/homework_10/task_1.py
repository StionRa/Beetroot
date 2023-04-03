#Function called oops that explicitly raises Index Error:
def oops():
    ob = IndexError
    raise  ob
def oops_two():
    er = KeyError
    raise er
#Function called another_function which calls the oops function:
def another_function():
    try:
        oops()
        #oops_two()
    except:
        print("Error caught")
# If we change oops() to raise Key Error instead of Index Error, then another_function() will also capture the KeyError.
# Споймает ошибку в любом случае
another_function()