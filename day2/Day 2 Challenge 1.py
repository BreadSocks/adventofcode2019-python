file = "input.txt"

program = [int(i) for i in open(file).read().split(",")]

if file == "input.txt":
    program[1] = 12
    program[2] = 2

index = 0
looping = True
while looping:
    op_code = program[index]
    if op_code == 99:
        looping = False
        break
    print(program)
    value1 = program[program[index + 1]]
    value2 = program[program[index + 2]]
    newLocation = program[index + 3]

    if op_code == 1:
        program[newLocation] = value1 + value2
    elif op_code == 2:
        program[newLocation] = value1 * value2

    index += 4

print(program)
