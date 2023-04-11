class CustomException(Exception):
    def __init__(self, msg):
        self.msg = msg
        with open("logs.txt", "a") as f:
            f.write(msg + "\n")
        super().__init__(msg)
    def __str__(self):
        return 'Value Error Text 2'



def fahrenheit_to_celsius(f: float) -> float:
    min_f = 32
    max_f = 212
    if f < min_f or f > max_f:
        raise CustomException ('There is not a valid range')

    return (f - 32) * 5 / 9


if __name__ == '__main__':
    f = input('Enter a temperature in Fahrenheit:')
    try:
        f = float(f)
    except ValueError as ex:
        print(CustomException("Value Error Text 1"))
    else:
        try:
            c = fahrenheit_to_celsius(float(f))
        except CustomException as ex:
            print(ex, "Text Test")
        else:
            print(f'{f} Fahrenheit = {c:.4f} Celsius')
