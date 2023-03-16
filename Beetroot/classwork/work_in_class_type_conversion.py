while True:
    what_to_convert = input("If you want to convert, enter 'C' for CMYK in RGB to convert or 'Exit' 'E' to exit: ").lower()
    try:
        if what_to_convert == 'c':
            try:
                cmyk_number = input(
                    "Enter a number with a dot 'float' for each parameter separated by a space'0.0 0.1 0.0 0.1': ")
                cmyk_number = cmyk_number.split()
                cyan = float(cmyk_number[0])
                magenta = float(cmyk_number[1])
                yellow = float(cmyk_number[2])
                black = float(cmyk_number[3])
                white = 1 - black
                red = 255 * white * (1 - cyan)
                green = 255 * white * (1 - magenta)
                blue = 255 * white * (1 - yellow)
                if red > 255 or green > 255 or blue > 255:
                    print("something is wrong with the numbers")
                    continue
                print('RGB color is \nred =', int(red), '\ngreen =', int(green), '\nblue =', int(blue))
            except ValueError:
                print("Something went wrong, please check your input.")
                continue
        elif what_to_convert == "exit" or what_to_convert == "e":
            print ("Okay")
            continue
        else:
            print('Not C or Exit or E')
            continue
    except ValueError:
        print("something is wrong with your input")
        continue