def process_file(file):
    total = 0
    engine_numbers = []
    symbol_locations = []

    line_arr = []
    with open(file) as f:
        for line in f:
            line_arr.append(line.rstrip())

    for line in line_arr:
        engine_numbers.append(find_engine_numbers(line))
        symbol_locations.append(find_symbol_locations(line))

    valid = valid_parts(engine_numbers, symbol_locations)
    for number in valid:
        total += int(number)

    return total


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

def find_symbol_locations(line):
    locations = []
    for index, char in enumerate(line):
        if char != "." and char.isdigit() == False:
            locations.append(index)

    return locations

# [[(0, '4'), (1, '6'), (2, '7')], [(5, '1'), (6, '1'), (7, '4')]]
# [[], [3]]

def valid_parts(eng_numbers, sym_locations):
    valid_numbers = []

    for line, numbers in enumerate(eng_numbers):
        valid = False

        for number in numbers:
            number_str = ""
            for index, digit in number:
                number_str = number_str + digit

                if line != 0:
                    for symbol in sym_locations[line-1]:
                        if index-1 <= symbol <= index+1:
                            valid = True

                for symbol in sym_locations[line]:
                    if index-1 <= symbol <= index+1:
                        valid = True

                if line != len(eng_numbers)-1:
                    for symbol in sym_locations[line+1]:
                        if index-1 <= symbol <= index+1:
                            valid = True

            if valid:
                valid_numbers.append(number_str)
                number_str = ""
                valid = False

    return valid_numbers
            

#print(valid_parts([[(0, '4'), (1, '6'), (2, '7')], [(5, '1'), (6, '1'), (7, '4')]], [[], [3]]))

#print(find_engine_numbers("..35..633."))
#print(find_symbol_locations("..35.*633."))

print(process_file("input.txt"))
