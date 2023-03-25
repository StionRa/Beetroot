# try:
#     #5/0
#     raise Exception('qweer', 'qweqwe', 'qwe')
# except Exception as ex:
#
#     print(ex.args)
# def test():
#     try:
#         #list = [1, 2, 3, 4]
#         a = 5 / 0
#         5 + '5'
#         #list[5]
#         return a
#
#
#     except ZeroDivisionError:
#         return 'Can`t division by 0'
#     except TypeError:
#         return "Tupe Error"
#     except IndexError:
#         return 'Index out of range'
#     except:
#         return "LOL"
#     finally:
#         return "finally Exit"
# print(test())


import json
with open('test.json') as file_object:
    # my_dict = {'name' : 'Stas', 'age' : 39}
    # json.dump(my_dict, file_object)
    test = json.load(file_object)
    for k, v in test.items():
        print(k, ':', v)