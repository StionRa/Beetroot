
def count_lines(name):
    with open(name) as f:
        return len(f.readlines())


def count_chars(name):
    with open(name) as f:
        return len(f.read())


# def test(name):
#     with open(name) as f:
#         line_1 = len(f.read())
#         f.seek(0)
#         line_2 = len(f.readlines())
#         f.close()
#     return line_2, line_1
# print(test('text.txt'))

def test(name):
    lines = count_lines(name)
    characters = count_chars(name)
    if lines == 0:
        return name, "Have no line!"
    elif characters == 0:
        return name, "Have no characters!"
    else:
        print(name, "have", lines, "lines and", characters, "characters")

test('text.txt')