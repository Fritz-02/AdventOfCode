from get_input import get_input

puzzle_input = get_input(2015, 1)


p1 = 0
p2 = None
for idx, char in enumerate(puzzle_input):
    p1 += 1 if char == "(" else -1
    if p2 is None and p1 < 0:
        p2 = idx + 1

print(p1)
print(p2)
