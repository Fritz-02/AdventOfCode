from get_input import get_input

puzzle_input = get_input(2023, 2)


bag = {"red": 12, "green": 13, "blue": 14}
sum_of_ids = 0
sum_of_power = 0
for game in puzzle_input.split("\n"):
    game_id, rounds = game.split(":")
    impossible = False
    max_cubes = {"red": 0, "green": 0, "blue": 0}
    for r in rounds.split(";"):
        for cube_set in r.split(","):
            amount, color = (s.strip() for s in cube_set.split())
            amount = int(amount)
            if amount > max_cubes[color]:
                max_cubes[color] = amount
            if not impossible and amount > bag[color]:
                impossible = True

    if not impossible:
        sum_of_ids += int(game_id[5:])

    sum_of_power += max_cubes["red"] * max_cubes["green"] * max_cubes["blue"]

print(sum_of_ids)
print(sum_of_power)
