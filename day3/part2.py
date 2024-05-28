def find_gear_locations(line):
    locations = []
    for index, char in enumerate(line):
        if char == "*":
            locations.append(index)

    return locations


def find_engine_numbers(line):
    part = []
    parts = []
    found = False
    for index, char in enumerate(line):
        
        if found == True and char.isdigit() == False:
            found = False
            parts.append(part)
            part = []

        if char.isdigit():
            found = True
            part.append((index, char))

    if found:
        parts.append(part)

    return parts

def find_valid_gears(gear_locations, engine_numbers):
    valid_gears = []
    for line, gears in enumerate(gear_locations):
        engine_count = 0
        engines = []
        for gear in gears:

            if line != 0:
                for numbers in engine_numbers[line-1]:
                    for number in numbers:
                        for i in range(gear-1, gear+2):
                            if i in number:
                                # Found number for gear
                                if numbers not in engines:
                                    engine_count += 1
                                    engines.append(numbers)
                            
            for numbers in engine_numbers[line]:
                for number in numbers:
                    for i in range(gear-1, gear+2):
                        if i in number:
                            if numbers not in engines:
                                engine_count += 1
                                engines.append(numbers)

            if line != len(gear_locations)-1:
                for numbers in engine_numbers[line+1]:
                    for number in numbers:
                        for i in range(gear-1, gear+2):
                            if i in number:
                                if numbers not in engines:
                                    engine_count += 1
                                    engines.append(numbers)

            if engine_count == 2:
                gear_values = []
                for eng in engines:
                    num = ""
                    for index, digit in eng:
                        num = num + digit
                    gear_values.append(num)

                valid_gears.append(gear_values)

                engine_count = 0
                engines = []
    print(valid_gears)
    return valid_gears


def process_file(file):
    line_arr = []
    total = 0
    with open(file) as f:
        for line in f:
            line_arr.append(line.rstrip() + ".")

    gear_locations = []
    engine_numbers = []
    for line in line_arr:
        gear_locations.append(find_gear_locations(line))
        engine_numbers.append(find_engine_numbers(line))

    valid_gears = find_valid_gears(gear_locations, engine_numbers)

    for gear in valid_gears:
        total += int(gear[0]) * int(gear[1])

    print(total)
#    print(gear_locations)
#    print(engine_numbers)

process_file("input.txt")
