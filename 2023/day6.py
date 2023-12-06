from get_input import get_input
import math


def calculate_ways_to_win(race_time: int, race_distance: int) -> int:
    a = (race_time**2 - 4 * race_distance) ** (1 / 2)
    b1 = int((race_time - a) / 2) + 1
    b2 = math.ceil((race_time + a) / 2) - 1
    return 1 + b2 - b1


times, distances = (
    line[line.index(":") + 1:].split() for line in get_input(2023, 6).split("\n")
)

p1 = 1
for t, d in zip(times, distances):
    p1 *= calculate_ways_to_win(int(t), int(d))

p2 = calculate_ways_to_win(int("".join(times)), int("".join(distances)))

print(p1)
print(p2)
