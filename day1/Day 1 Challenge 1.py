fuel = 0
with open("input.txt") as inputFile:
    for line in inputFile:
        line = line.replace("\n", "")
        number = int(line)
        fuel += (int(number / 3) - 2)
print(fuel)
