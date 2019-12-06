import itertools

file = "input.txt"

# possible = list(itertools.product(range(100), repeat=2))
# possible_index = 0

program = [int(i) for i in open(file).read().split(",")]

found_number = False
input_value = 1

# while not found_number:
new_program = list(program)
# new_program[1] = possible[possible_index][0]
# new_program[2] = possible[possible_index][1]

index = 0
looping = True
while looping:
    instruction = new_program[index]
    instruction_values = [int(x) for x in str(instruction)]
    instruction_offset = 1
    if len(instruction_values) == 1:
        op_code = instruction
    elif int(str(instruction)[-2:]) < 10:
        op_code = int(str(instruction)[-2:])
        instruction_offset = 2
    elif int(str(instruction)[-2:]) == 99:
        looping = False
        break
    else:
        op_code = instruction_values[-1]

    first_position_mode = 0
    second_position_mode = 0
    third_position_mode = 0

    if len(instruction_values) == 3:
        if instruction_offset == 2:
            first_position_mode = instruction_values[0]
        else:
            first_position_mode = instruction_values[1]
            second_position_mode = instruction_values[0]
    elif len(instruction_values) == 4:
        if instruction_offset == 2:
            first_position_mode = instruction_values[1]
            second_position_mode = instruction_values[0]
        else:
            first_position_mode = instruction_values[2]
            second_position_mode = instruction_values[1]
            third_position_mode = instruction_values[0]
    elif len(instruction_values) == 5:
        first_position_mode = instruction_values[2]
        second_position_mode = instruction_values[1]
        third_position_mode = instruction_values[0]

    if op_code == 1:
        if first_position_mode == 0:
            value1 = new_program[new_program[index + 1]]
        else:
            value1 = new_program[index + 1]

        if second_position_mode == 0:
            value2 = new_program[new_program[index + 2]]
        else:
            value2 = new_program[index + 2]

        newLocation = new_program[index + 3]
        new_program[newLocation] = value1 + value2
        index += 4
    elif op_code == 2:
        if first_position_mode == 0:
            value1 = new_program[new_program[index + 1]]
        else:
            value1 = new_program[index + 1]

        if second_position_mode == 0:
            value2 = new_program[new_program[index + 2]]
        else:
            value2 = new_program[index + 2]

        newLocation = new_program[index + 3]
        new_program[newLocation] = value1 * value2
        index += 4
    elif op_code == 3:
        newLocation = new_program[index + 1]
        new_program[newLocation] = input_value
        index += 2
    elif op_code == 4:
        newLocation = new_program[index + 1]
        # print("Output: " + str(new_program[index + 1]))
        print("Output: " + str(new_program[new_program[index + 1]]))
        index += 2
    else:
        print("shit found an opcode i don't know: " + op_code)

print("broke out and im here")
