import string

# Read entire file - into list of lines.
with open('input.txt') as f:
    lines = f.readlines()

total = 0

# Process each line

for l in lines:

    # remove any trailing '\n'
    if l[-1] == '\n':
        l = l[:-1]

    print('\nlooking at line "', l, '"')

    # Split into two halves.
    first = l[:len(l)//2]
    second = l[len(l)//2:]

    print('first  ', first)
    print('second ', second)

    # Make strings into set of characters.

    chars_one = set(first)
    chars_two = set(second)

    print('set one is ', chars_one)
    print('set two is ', chars_two)

    # Find common character.
    result = chars_one.intersection(chars_two)

    if len(result) != 1:
        # Should be only one common character.
        print("ERROR: union set is of length ", len(result), " which is wrong. Set is ", result)

    # Make it an actual character.
    the_char = next(iter(result))
    print('common char is ', the_char)

    # Map to priority number: 'a' -> 'z' is 1..26 and 'A'..'Z' is 27...
    if the_char in string.ascii_lowercase:
        priority = ord(the_char) - ord('a') + 1
    elif the_char in string.ascii_uppercase:
        priority = ord(the_char) - ord('A') + 27
    else:
        print('ERROR: invalid character ', the_char)

    print('char ', the_char, ' has priority of ', priority)

    # Keep a total count.
    total += priority

    print('new priority is ', total)

print('Grand Total is ', total)
