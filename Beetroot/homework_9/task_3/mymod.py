
def count_lines(name):
    with open(name) as f:
        return len(f.readlines())

print(count_lines('text.txt'))


def count_chars(name):
    with open(name) as f:
        return len(f.read())
print(count_chars('text.txt'))


# def test(name):
#     with open(name) as f:
#         line_1 = len(f.read())
#         f.seek(0)
#         line_2 = len(f.readlines())
#         f.close()
#     return line_2, line_1
# print(test('text.txt'))

def test(name):
    return count_lines(name), count_chars(name)

print(test('text.txt'))