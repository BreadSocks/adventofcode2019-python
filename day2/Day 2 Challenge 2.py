import itertools

file = "input.txt"

possible = list(itertools.product(range(100), repeat=2))
possible_index = 0

program = [int(i) for i in open(file).read().split(",")]

found_number = False

while not found_number:
    new_program = list(program)
    new_program[1] = possible[possible_index][0]
    new_program[2] = possible[possible_index][1]

    index = 0
    looping = True
    while looping:
        op_code = new_program[index]
        if op_code == 99:
            looping = False
            break
        # print(program)
        value1 = new_program[new_program[index + 1]]
        value2 = new_program[new_program[index + 2]]
        newLocation = new_program[index + 3]

        if op_code == 1:
            new_program[newLocation] = value1 + value2
        elif op_code == 2:
            new_program[newLocation] = value1 * value2

        index += 4
    print("broke out and im here")
    if new_program[0] == 19690720:
        print("Found program")
        found_number = True
    else:
        possible_index += 1

noun = possible[possible_index][0]
verb = possible[possible_index][1]
print("Noun: " + str(noun)
      + "\nVerb: " + str(verb)
      + "\nValue: " + str((100 * noun) + verb))
