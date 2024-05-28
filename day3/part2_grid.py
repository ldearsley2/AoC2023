class GearFinder:

    DIRECTIONS_TO_CHECK = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]

    def __init__(self, gear_file):
        self.gear_file = [list(line) for line in gear_file.split("\n")]
        self.checked_locations = set()

    def sum_gears(self):
        total = 0
        for row_index, row in enumerate(self.gear_file):
            for char_index, char in enumerate(row):
                if char == "*":
                    total += self.get_ratio(row_index, char_index)

        return total

    def get_ratio(self, row, column):
        adjacent_numbers = []
        for x, y in self.DIRECTIONS_TO_CHECK:
            adjacent_row, adjacent_column = row + x, column + y
            if 0 <= adjacent_row < len(self.gear_file) and 0 <= adjacent_column < len(
                self.gear_file[adjacent_row]
            ):
                if self.gear_file[adjacent_row][adjacent_column].isdigit():
                    part_number = self.get_full_number(adjacent_row, adjacent_column)
                    if part_number not in adjacent_numbers:
                        adjacent_numbers.append(part_number)

        if len(adjacent_numbers) == 2:
            return adjacent_numbers[0] * adjacent_numbers[1]

        return 0

    def get_full_number(self, row, column):
        full_number = self.gear_file[row][column]

        left_col = column - 1
        while left_col >= 0 and self.gear_file[row][left_col].isdigit():
            full_number = self.gear_file[row][left_col] + full_number
            left_col -= 1

        right_col = column + 1
        while (
            right_col < len(self.gear_file[row])
            and self.gear_file[row][right_col].isdigit()
        ):
            full_number = full_number + self.gear_file[row][right_col]
            right_col += 1

        return int(full_number)


def create_input_grid(file):
    with open(file) as f:
        output_grid = f.read()

    return output_grid


gear_finder = GearFinder(create_input_grid("input.txt"))

total = gear_finder.sum_gears()

print(total)
