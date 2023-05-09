from stacks_queues import Stack


# # create an instance of Stack class
# stack = Stack()
#
# # read in the sequence of characters
# sequence = input("Enter a sequence of characters: ")
#
# # push each character onto the stack
# for char in sequence:
#     stack.push(char)
#
# # pop each character from the stack and print them
# print("".join([stack.pop() for i in range(stack.size())]))
#

# создаем экземпляр класса Stack
stack = Stack()

# считываем последовательность символов
sequence = input("Введите последовательность символов: ")

# определяем открытые и закрытые скобки
open_brackets = "([{"
close_brackets = ")]}"

# перебираем каждый символ в последовательности
for char in sequence:
    # если символ - открывающая скобка, помещаем ее на вершину стека
    if char in open_brackets:
        stack.push(char)
    # если символ - закрывающая скобка, проверяем, что на вершине стека соответствующая открывающая скобка
    elif char in close_brackets:
        # если стек пустой, или на вершине стека нет соответствующей открывающей скобки, то скобки не сбалансированы
        if stack.is_empty() or open_brackets.index(stack.peek()) != close_brackets.index(char):
            print("Скобки не сбалансированы.")
            break
        # если на вершине стека соответствующая открывающая скобка, удаляем ее из стека
        stack.pop()
else:
    # если стек пустой, то скобки сбалансированы
    if stack.is_empty():
        print("Скобки сбалансированы.")
    else:
        print("Скобки не сбалансированы.")

