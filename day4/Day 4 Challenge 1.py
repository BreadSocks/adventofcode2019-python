possibilities = range(172930, 683082 + 1)
possible_passwords = []
for p in possibilities:
    numbers = [int(x) for x in str(p)]
    increasing_found = all(i <= j for i, j in zip(numbers, numbers[1:]))
    doubles_found = any(i == j for i, j in zip(numbers, numbers[1:]) )
    if increasing_found and doubles_found:
        possible_passwords.append(p)
print((len(possible_passwords)))
