nums = []
for i in range (3, 323):
    if i %13 == 0:
        nums.append(i)
print(tuple(nums))