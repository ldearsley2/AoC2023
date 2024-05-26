# 12 red, 13 green, 14 blue

colour_count = {
        "red": 12,
        "green": 13,
        "blue": 14
        }

def check_game(game):
    game_id, rounds = game.split(":")
    game_id = game_id.split()[1]
    rounds = rounds.split(";")
    rounds = [round.strip() for round in rounds]
    for round in rounds:
        cubes = round.split(",")
        for cube in cubes:
            count, colour = cube.split()
            if int(count) > colour_count[colour]:
                return 0

    return int(game_id)

def get_total(file):
    total = 0
    with open(file) as f:
        for game in f:
            total += check_game(game)

    return total

print(check_game("Game 10: 5 red, 1 green, 2 blue; 2 green, 8 blue, 6 red; 8 red, 3 blue, 2 green; 6 red, 1 green, 10 blue; 1 red, 10 blue"))

print(get_total("input.txt"))
