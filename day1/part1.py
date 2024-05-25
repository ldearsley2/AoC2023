def part1(file):
    total = 0
    with open(file) as f:
        for line in f:
           first = ""
           last = ""
           
           for char in line:
               if char.isdigit():
                   if first == "":
                       first, last = char, char
                   else:
                       last = char


           val = int(f"{first}{last}")
           total += val

    return total

print(part1("input.txt"))
