import sys

print(sys.path)

sys.path.append('qwerty')
print(sys.path)
sys.path.remove('qwerty')
print(sys.path)
sys.path.append('qwerty')
print(sys.path.count('qwerty'))