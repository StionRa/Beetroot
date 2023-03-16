import random
steps = 0
x, y = 0, 0
cardinal_directions = ['Nord', 'South', 'East', 'West']
n_point = int(input("square: "))
while abs(x) < n_point and abs(y) < n_point:
    step = random.choice(cardinal_directions)
    if step == "Nord":
        x += 1
    elif step == "South":
        x -= 1
    elif step == "East":
        y += 1
    elif step == "West":
        y -= 1
    steps += 1

print("Steps: ", steps, "\nx, y: ", x, y)
