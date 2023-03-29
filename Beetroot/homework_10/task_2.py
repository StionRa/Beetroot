def user_input():
    try:
        a = int(input("enter first digit: "))
        b = int(input("enter second digit: "))
        x = (a ** 2) / b
    except ZeroDivisionError:
        raise
        #print("Sorry ! You are dividing by zero ")
    except ValueError:
        raise
        #print("invalid literal for int() with base 10: ''")
    else:
        print("Yeah ! Your answer is :", x)


user_input()