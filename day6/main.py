def get_hold_times(distance: int, time: int):
    total = 0
    for i in range(time + 1):
        hold_time = i
        remaining_time = time - hold_time

        if hold_time * remaining_time > distance:
            total += 1

    return total


def main():
    times = []
    distances = []
    with open("input.txt") as f:
        for i, line in enumerate(f):
            if i == 0:
                times = line.split(":")[1].strip().split()
            else:
                distances = line.split(":")[1].strip().split()

    total = 0

    for i, distance in enumerate(distances):
        if i == 0:
            total += get_hold_times(int(distance), int(times[i]))
        else:
            total *= get_hold_times(int(distance), int(times[i]))

    part2_time = "".join(times)
    part2_distance = "".join(distances)

    part2_total = get_hold_times(int(part2_distance), int(part2_time))

    print(total)
    print(part2_total)


main()
