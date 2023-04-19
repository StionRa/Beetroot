person = {
    "Person": [{"first_name": "Stas", "last_name": "Zelinskyi", "birthday": "09.08.1983", "age": 39, "sex": "female",
                "height": 1.80, "weight": 64, "body_type": "ectomorph", "target_weight": 80, "time_to_goal": 90,
                "activity_level": "light", "bmi": None}]}


def bmi_level():
    for x in person['Person']:
        height = x["height"]
        weight = x["weight"]
        formula = weight / (height ** 2)
        return formula


def formula_bmi(level):
    for x in person["Person"]:
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


def mifflin():
    for x in person["Person"]:
        if x["sex"] == 'male':
            if x["activity_level"] == 'low':
                miff = (10 * x['weight']) + ((6.25 * (x["height"] * 100) + (5 * x["age"]) + 5) * 1.2)
            elif x["activity_level"] == 'light':
                miff = (10 * x['weight']) + ((6.25 * (x["height"] * 100) + (5 * x["age"]) + 5) * 1.375)
            elif x["activity_level"] == 'training':
                miff = (10 * x['weight']) + ((6.25 * (x["height"] * 100) + (5 * x["age"]) + 5) * 1.55)
            elif x["activity_level"] == 'intense':
                miff = (10 * x['weight']) + ((6.25 * (x["height"] * 100) + (5 * x["age"]) + 5) * 1.725)
            elif x["activity_level"] == 'max_intence':
                miff = (10 * x['weight']) + ((6.25 * (x["height"] * 100) + (5 * x["age"]) + 5) * 1.9)
            else:
                print("Something wrong for male")
                exit()
        elif x["sex"] == 'female':
            if x["activity_level"] == 'low':
                miff = (10 * x['weight']) + ((6.25 * (x["height"] * 100) + (5 * x["age"]) - 161) * 1.2)
            elif x["activity_level"] == 'light':
                miff = (10 * x['weight']) + ((6.25 * (x["height"] * 100) + (5 * x["age"]) - 161) * 1.375)
            elif x["activity_level"] == 'training':
                miff = (10 * x['weight']) + ((6.25 * (x["height"] * 100) + (5 * x["age"]) - 161) * 1.55)
            elif x["activity_level"] == 'intense':
                miff = (10 * x['weight']) + ((6.25 * (x["height"] * 100) + (5 * x["age"]) - 161) * 1.725)
            elif x["activity_level"] == 'max_intence':
                miff = (10 * x['weight']) + ((6.25 * (x["height"] * 100) + (5 * x["age"]) - 161) * 1.9)
            else:
                print("Something wrong for female")
                exit()
        else:
            print("Something wrong with everithing")
            exit()
        return miff


for x in person['Person']:
    exp = x['target_weight'] - x['weight']
    new_ballance = (exp * 7000 / x['time_to_goal']) / 1.55
    target = mifflin() * 1.55 + new_ballance
    print(f'{int(target)} you need every day')

formula_bmi(bmi_level())
mifflin()
