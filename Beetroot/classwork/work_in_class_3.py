# # 5. В циклі while задайте умову для проходження змінної my_number від 1 до 25 (при кожному проході виводьте на прінт значення
# # my_number),
# # але зупиніть виконання коли my_number буде ділитись без остачі на 3 і на 7.
# my_number = 1
# while(my_number < 25):
#     print(my_number)
#     if my_number // 3 != 0 and my_number // 7 != 0:
#         break
#     else:
#         my_number+=1


# Виведіть з допомогою циклу for всі літери з ‘qwerty’
#
# for i in "python":
#     print(i)
#
# for count, value in enumerate('python', start=1):
#     print(count, value)

# Task 1
# Write a Python program to convert temperatures to and from celsius, Fahrenheit.
# Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in Fahrenheit
# Expected Output (pay attention to output, students have to practice in string formating for constructing result message):
# 60°C is 140 in Fahrenheit
# 45°F is 7 in Celsius

celsius_text = 'in Celsius'
celsius_sign = '°C'
fahrenheit_text = 'in Fahrenheit'
fahrenheit_sign = '°F'
greeting_text = "Fahrenheit to Celsius conversion and vice versa degrees Celsius to degrees Fahrenheit"
print(greeting_text)
select_scale = input("\nselect measurement scale C (celsius) or F (fahrenheit): ").lower()
if select_scale == 'c':
    enter_amount = input('Enter amount in int: ')
    if enter_amount.isdigit():
        enter_amount = float(enter_amount)
        conversion_fahrenheit = (int(enter_amount) - 32)/1.8
        print(round(enter_amount, 1), fahrenheit_sign, 'is', round(conversion_fahrenheit, 1), 'in', celsius_sign)
    else:
        print("enter correct values 1")
elif select_scale == 'f':
    enter_amount = input('Enter amount in int: ')
    if enter_amount.isdigit():
        enter_amount = float(enter_amount)
        conversion_celsium = int(enter_amount)*1.8+32
        print(round(enter_amount, 1), celsius_sign, 'is', round(conversion_celsium, 1), 'in', fahrenheit_sign)
    else:
        print("enter correct values 2")
else:
    print("enter correct values 3")



