word_to_num = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
        }

def get_digits(line) -> int:
    digits = []
    for word, num in word_to_num.items():
        for i in range(len(line)):
            if line.startswith(word, i):
                digits.append((i, word_to_num[word]))


    digits.extend((index, char) for index, char in enumerate(line) if char.isdigit())

    digits.sort(key=lambda x: x[0])

    return int(f"{digits[0][1]}{digits[-1][1]}")

def process_file(file) -> int:
    total = 0
    with open(file) as f:
        for line in f:
            total += get_digits(line)

    return total

print(get_digits("6798sevenine"))

print(process_file("input.txt"))
