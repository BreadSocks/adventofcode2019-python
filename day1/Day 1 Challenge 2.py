fuel = 0
with open("input.txt") as inputFile:
    for line in inputFile:
        line = line.replace("\n", "")
        number = int(line)
        module_fuel = (int(number / 3) - 2)
        additional_fuel = (int(module_fuel / 3) - 2)
        needs_more_fuel = additional_fuel > 0
        while needs_more_fuel:
            print("needs additional fuel: " + str(additional_fuel))
            module_fuel += additional_fuel
            additional_fuel = (int(additional_fuel / 3) - 2)
            needs_more_fuel = additional_fuel > 0
        print("module: " + str(module_fuel))
        fuel += module_fuel

print(fuel)
