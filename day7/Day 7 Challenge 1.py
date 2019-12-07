import itertools

file = "input.txt"
program = [int(i) for i in open(file).read().split(",")]
results = dict()
# input_value = 0

new_program = list(program)
permutations_index = 0


# looping = True

def execution(input_values):
    index = 0
    new_program = list(program)
    looping = True
    output = 0
    while looping:
        print(new_program)
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
            print("opcode 1: " + str(value1) + " and " + str(value2) + " to go in position " + str(newLocation))
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
            input_value = input_values.pop(0)
            new_program[newLocation] = input_value
            print("opcode 3: " + str(input_value) + " into position " + str(newLocation))
            index += 2
        elif op_code == 4:
            if first_position_mode == 0:
                value1 = new_program[new_program[index + 1]]
            else:
                value1 = new_program[index + 1]

            print("Output: " + str(value1))
            output = value1
            index += 2
        elif op_code == 5:
            if first_position_mode == 0:
                value1 = new_program[new_program[index + 1]]
            else:
                value1 = new_program[index + 1]

            if second_position_mode == 0:
                value2 = new_program[new_program[index + 2]]
            else:
                value2 = new_program[index + 2]

            if value1 != 0:
                index = value2
            else:
                index += 3
        elif op_code == 6:
            if first_position_mode == 0:
                value1 = new_program[new_program[index + 1]]
            else:
                value1 = new_program[index + 1]

            if second_position_mode == 0:
                value2 = new_program[new_program[index + 2]]
            else:
                value2 = new_program[index + 2]

            if value1 == 0:
                index = value2
                print("opcode 6: " + str(value1) + " is 0 so " + str(value2) + " is new index")
            else:
                print("opcode 6: " + str(value1) + " is not 0 so incrementing by 3")
                index += 3
        elif op_code == 7:
            if first_position_mode == 0:
                value1 = new_program[new_program[index + 1]]
            else:
                value1 = new_program[index + 1]

            if second_position_mode == 0:
                value2 = new_program[new_program[index + 2]]
            else:
                value2 = new_program[index + 2]

            newLocation = new_program[index + 3]

            if value1 < value2:
                new_program[newLocation] = 1
            else:
                new_program[newLocation] = 0
            index += 4
        elif op_code == 8:
            if first_position_mode == 0:
                value1 = new_program[new_program[index + 1]]
            else:
                value1 = new_program[index + 1]

            if second_position_mode == 0:
                value2 = new_program[new_program[index + 2]]
            else:
                value2 = new_program[index + 2]

            newLocation = new_program[index + 3]

            if value1 == value2:
                new_program[newLocation] = 1
            else:
                new_program[newLocation] = 0
            index += 4
        else:
            print("shit found an opcode i don't know: " + op_code)
    return output


# test1 = [1, 0, 4, 3, 2]
# input_output = 0
# for digit in test1:
#     input_output = execution([digit, input_output])
#     results[digit] = input_output
# print(results)
# print("result: " + str(input_output))

permutations = list(itertools.permutations(range(5), 5))
# permutations = [[1, 0, 4, 3, 2]]
for permutation in permutations:
    input_output = 0
    for digit in permutation:
        input_output = execution([digit, input_output])
    results[str(permutation)] = input_output
    print(results)

print("max found:" + str(max(results.values())))
print("broke out and im here")
