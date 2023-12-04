from get_input import get_input

puzzle_input = get_input(2015, 2)


p1 = 0
p2 = 0
for box in puzzle_input.split("\n"):
    l, w, h = (int(x) for x in box.split("x"))
    sides = l * w, w * h, h * l
    p1 += sum(2 * sides) + min(sides)
    p2 += sum(sorted((l, w, h))[:2] * 2) + l * w * h

print(p1)
print(p2)
