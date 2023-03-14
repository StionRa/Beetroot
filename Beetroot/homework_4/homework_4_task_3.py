question = int(input('2 + 2 = '))
if question == 4:
    print (True)
else:
    print(False)




# print("The math quiz program.")
#
# score = 0
# question_no = 0
# text = ' Question '
# playing = input('Do you want to play ? (Y/N)').lower()
#
# if playing == 'y':
#     question_no += 1
#     ques = input(f'\n{question_no}{text} 2 + 2 =').lower()
#     if ques == '4':
#         score += 1
#         print('correct! you got 1 point')
#
#     else:
#         print('Incorrect!')
#         print(f'current answer is --> 4')
#
#
#     question_no += 1
#     ques = input(f'\n{question_no}{text} 6 * 6 = ').lower()
#
#     if ques == '36':
#         score += 1
#         print('correct! you got 1 point')
#
#     else:
#         print('Incorrect!')
#         print(f'current answer is --> 36')
#
#     # -----2
#     question_no += 1
#     ques = input(f'\n{question_no}{text} 2 + 2 * 3 ').lower()
#
#     if ques == '8':
#         score += 1
#         print('correct! you got 1 point')
#
#     else:
#         print('Incorrect!')
#         print(f'current answer is --> 8')
#
#     # -----3
#     question_no += 1
#     ques = input(f'\n{question_no}{text} 2 / 2 * 3 ').lower()
#
#     if ques == '3':
#         score += 1
#         print('correct! you got 1 point')
#
#     else:
#         print('Incorrect!')
#         print(f'current answer is --> 3')
#
#     # -----4
#     question_no += 1
#     ques = input(f'\n{question_no}{text} 15 % 5 ').lower()
#
#     if ques == '0':
#         score += 1
#         print('correct! you got 1 point')
#
#     else:
#         print('Incorrect!')
#         print(f'current answer is --> 0')
#
#
# # ------5
#
# else:
#     print('thankyou you are out of a game.')
#     quit()
#
# print(f'\nnumber of question is {question_no}')
# print(f'your score is {score}')