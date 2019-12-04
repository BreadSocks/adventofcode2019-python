def chunky(list_of_ints):
    for i in range(0, len(list_of_ints), 2):
        yield list_of_ints[i:i + 2]

possibilities = range(172930, 683082 + 1)
possible_passwords = []
for p in possibilities:
    numbers = [int(x) for x in str(p)]
    increasing_found = all(i <= j for i, j in zip(numbers, numbers[1:]))

    if not increasing_found:
        continue

    doubles_found = any(i == j for i, j in zip(numbers, numbers[1:]))

    if not doubles_found:
        continue

    occurrences = dict()
    for i in numbers:
        if i in occurrences:
            occurrences[i] += 1
        else:
            occurrences[i] = 1

    occurrences_count = list(occurrences.values())
    if 2 not in occurrences_count:
        continue

    possible_passwords.append(p)
print(possible_passwords)
print((len(possible_passwords)))
