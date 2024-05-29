def process_scratchcards_partone(file):
    card_numbers = []
    winning_numbers = []
    with open(file) as f:
        for line in f:
            card_number, winning_number = line.split("|")
            card_numbers.append(card_number.split(":")[1].strip().split())
            winning_numbers.append(winning_number.strip().split())

    #    print(f"card numbers: {card_numbers}, winning numbers: {winning_numbers}")
    total_points = 0
    for i in range(len(card_numbers)):
        total_points += calculate_points(card_numbers[i], winning_numbers[i])

    return total_points


def calculate_points(card_nums, winning_nums):
    total_nums = 0
    for card_num in card_nums:
        if card_num in winning_nums:
            total_nums += 1

    points = 0
    if total_nums >= 1:
        points += 1
        for i in range(total_nums - 1):
            points *= 2

    return points


# print(process_scratchcards_partone("input.txt"))


def process_scratchcards_parttwo(file):
    card_numbers = []
    winning_numbers = []
    with open(file) as f:
        for line in f:
            card_number, winning_number = line.split("|")
            card_numbers.append(card_number.split(":")[1].strip().split())
            winning_numbers.append(winning_number.strip().split())

    card_winning_numbers = {}
    for i, numbers in enumerate(card_numbers):
        card_winning_numbers[i + 1] = calculate_winners(
            card_numbers[i], winning_numbers[i]
        )

    card_store = {}
    for i in range(len(card_numbers)):
        card_store[i + 1] = 1

    for k, v in card_winning_numbers.items():
        pass

    print(card_store)


def calculate_winners(card_nums, winning_nums):
    total_nums = 0
    for card_num in card_nums:
        if card_num in winning_nums:
            total_nums += 1

    return total_nums


print(process_scratchcards_parttwo("test_input.txt"))
