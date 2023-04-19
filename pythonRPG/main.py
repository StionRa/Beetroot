import json
import os
import uuid

filename = "data_person.json"


def create_file(new_data):
    if not os.path.exists(filename):
        data = {"Person": [new_data]}
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
    elif os.path.getsize(filename) == 0:
        data = {"Person": [new_data]}
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
    elif os.path.exists(filename) and os.path.getsize(filename) > 0:
        # Read the current data from the file
        with open(filename, "r") as file:
            current_data = json.load(file)
        # Append the new data to the current data
        current_data["Person"].append(new_data)
        # Write the updated data back to the file
        with open(filename, "w") as f:
            json.dump(current_data, f, indent=4)
    else:
        return "something wrong"


def open_file():
    with open(filename, "r") as file:
        data = json.load(file)


def new_person():
    choise = input('''
    Good afternoon:
    1. Register
    2. Login
    3. Exit
    => ''')
    if choise == "1":
        print('''
        input your information in the form below''')
        person_id = str(uuid.uuid4())
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        birthday = input("Your birthday dd.mm.yyyy: ")
        age = int(input("Your age: "))
        sex = input("Your sex male or female: ")
        email = input("Your email: ")
        password = input("Your password: ")
        height = float(input("Your Height in meters if you 180 cm input 1.80: "))
        weight = int(input("You weight in kg: "))
        body_type = input("Input your body type - Ectomorph, Mesomorph, Ecto_mesomorph, Endpmorph: ")
        activity_level = input("Enter your activity - low, light, training, intense, maximum intensity: ")
        target_weight = int(input("What weight you want to have after training? "))
        time_to_goal = int(input("what period of time you want to achieve the desired result. "
                                 "You need to enter the number of days: "))

        new_data = {"ID": person_id, "first_name": first_name, "last_name": last_name, "birthday": birthday,
                    "age": age, "sex": sex, "email": email, "password": password, "Fitness_Data":
                        [{"height": height, "weight": weight, "body_type": body_type,
                          "target_weight": target_weight,
                          "time_to_goal": time_to_goal, "activity_level": activity_level, "bmi": None,
                          "miffin": None, "kkal_need": None}]}
        create_file(new_data)
    elif choise == "2":
        pass
    else:
        print("Wrong Value")


def bmi_level():
    with open(filename, "r") as file:
        data = json.load(file)
        for x in data['Person']:
            for y in x["Fitness_Data"]:
                height = y["height"]
                weight = y["weight"]
                formula = weight / (height ** 2)
                with open(filename, "r") as file:
                    data = json.load(file)
                    for x in data["Person"]:
                        for y in x["Fitness_Data"]:
                            y["bmi"] = round(formula, 2)
                            with open(filename, "w") as file:
                                json.dump(data, file, indent=4)

                return round(formula, 2)


def formula_bmi(level):
    with open(filename, "r") as file:
        data = json.load(file)
        for x in data["Person"]:
                if x["sex"] == 'male':
                    if 18 <= x['age'] <= 24:
                        normal_range = (19, 24)
                    elif 25 <= x['age'] <= 34:
                        normal_range = (20, 25)
                    elif 35 <= x['age'] <= 44:
                        normal_range = (21, 26)
                    elif 45 <= x['age'] <= 54:
                        normal_range = (22, 27)
                    elif 55 <= x['age'] <= 64:
                        normal_range = (23, 28)
                    else:
                        print("Данный возраст не входит в диапазон для мужчин.")
                        exit()
                elif x["sex"] == "female":
                    if 18 <= x['age'] <= 24:
                        normal_range = (19, 23)
                    elif 25 <= x['age'] <= 34:
                        normal_range = (20, 25)
                    elif 35 <= x['age'] <= 44:
                        normal_range = (21, 26)
                    elif 45 <= x['age'] <= 54:
                        normal_range = (22, 27)
                    elif 55 <= x['age'] <= 64:
                        normal_range = (23, 28)
                    else:
                        print("Данный возраст не входит в диапазон для женщин.")
                        exit()
                else:
                    print("Некорректно указан пол. Введите 'м' для мужского пола или 'ж' для женского пола.")
                    exit()
                if level < normal_range[0]:
                    category = "недостаточный вес"
                elif normal_range[0] <= level <= normal_range[1]:
                    category = "нормальный вес"
                else:
                    category = "избыточный вес или ожирение"
                print("Ваш ИМТ составляет {:.1f}".format(level))
                print("Нормальный диапазон ИМТ для вашего пола и возраста: {}-{}".format(normal_range[0], normal_range[1]))
                print("Ваша категория массы тела: {}".format(category))


def calculate():
    pass


# new_person()
print(bmi_level())
print(formula_bmi(bmi_level()))