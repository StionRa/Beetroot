import unittest
import os
import mymod
import sys
sys.path.append('/home/stanislavus/Python')


from slave import function_alpha as f
#os.mkdir('test')
#os.rmdir('test')
#print(os.listdir())

print(f(2, 5))
# file_my = open('mymod.py', 'r')
# print("File name: ", file_my.name)
# line = file_my.readlines()
# print('read line: %s' % (line))
print(mymod.count_lines('text.txt'))

unittest.main()