def modify_string(s):
    # Initialize variables
    prev_char = s[0]
    count = 1
    result = []

    # Iterate over the string
    for i in range(1, len(s)):
        if s[i] == prev_char:
            count += 1
        else:
            result.append((count, int(prev_char)))
            prev_char = s[i]
            count = 1

    # Add the last character to the result
    result.append((count, int(prev_char)))

    # Format the result as a string
    result_str = " ".join(["({}, {})".format(count, char) for count, char in result])

    return result_str

# Test the function
s = input()
print(modify_string(s))  # (1, 1) (3, 2) (1, 3) (2, 1)
