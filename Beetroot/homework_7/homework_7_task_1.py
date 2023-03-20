some_string = {}
string_text = input("Enter some string 'text': ")
list_of_words = string_text.split()
for word in list_of_words:
    some_string[word] = some_string.get(word, 0) + 1
print('Word Frequency')
for key in some_string.keys():
    print(key, some_string[key])
print(some_string)