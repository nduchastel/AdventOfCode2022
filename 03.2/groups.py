import string

# Read entire file into list of lines.
with open('input.txt') as f:
    lines = f.readlines()

total = 0

# Split into list of 3 lines:
#    rangs(0, len(lines), 3) -> 0, 3, 6, 9,...
groups = [lines[i:i+3] for i in range(0, len(lines), 3)]

print('found ', len(groups), ' number of groups')

# Process each grouo of 3 lines.
for g in groups:
    print('\ngroup is ', g)

    # make each string into a set (removing last char which should be '\n').
    chars_one = set(g[0][:-1])
    chars_two = set(g[1][:-1])
    chars_three = set(g[2][:-1])

    print('set one   is ', chars_one)
    print('set two   is ', chars_two)
    print('set three is ', chars_three)

    # Set intersection.
    common = chars_one.intersection(chars_two, chars_three)
    if len(common) != 1:
        print('ERROR: invalid group! not just 1 common character!')

    # Get the one and only character.
    the_char = next(iter(common))

    print('common character is ', the_char)

    # Map to priority.
    if the_char in string.ascii_lowercase:
        priority = ord(the_char) - ord('a') + 1
    elif the_char in string.ascii_uppercase:
        priority = ord(the_char) - ord('A') + 27
    else:
        print('ERROR: invalid character ', the_char)

    print('priority for ', the_char, ' is ', priority)

    # Keep a runming total.
    total += priority
    print('new priority is ', total)


print('Grand Total is ', total)
