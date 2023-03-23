import unittest
def count_lines(name):
    with open (name, 'r') as text:
        return len(text.readlines())

def count_chars(name):
    with open(name, 'r') as text:
        return len(text.read())

def test(name):
    file = open('text.txt', 'r')
    print("count lines: ", len(file.readlines()))
    file.close()
    file = open('text.txt', 'r')
    print('count chars: ', len(file.read()))
    file.close()
    return

if __name__ == '__main__':
    unittest.main()