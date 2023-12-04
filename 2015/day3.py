from get_input import get_input

puzzle_input = get_input(2015, 3)


direction_conversion = {"^": (0, 1), "v": (0, -1), ">": (1, 0), "<": (-1, 0)}
visited1 = {(0, 0)}
visited2 = {(0, 0)}
pos1 = (0, 0)
pos2 = (0, 0)
pos3 = (0, 0)
for n, direction in enumerate(puzzle_input):
    x, y = direction_conversion[direction]
    pos1 = (pos1[0] + x, pos1[1] + y)
    if n % 2:  # robo-santa
        pos2 = (pos2[0] + x, pos2[1] + y)
    else:  # santa
        pos3 = (pos3[0] + x, pos3[1] + y)
    visited1.add(pos1)
    visited2.add(pos2)
    visited2.add(pos3)

p1 = len(visited1)
p2 = len(visited2)

print(p1)
print(p2)
