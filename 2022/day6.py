from get_input import get_input

puzzle_input = get_input(filename=__file__)


p1 = None
p2 = None
i = 4
while p1 is None or p2 is None:
    if p1 is None and len(set(puzzle_input[i - 4:  i])) == 4:
        p1 = i
    if p2 is None and len(set(puzzle_input[max(0, i - 14): i])) == 14:
        p2 = i
    i += 1

print(p1)
print(p2)
