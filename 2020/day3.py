from get_input import get_input
from functools import reduce

puzzle_input = get_input(2020, 3)


lines = puzzle_input.split("\n")
length = len(lines[0])
trees = []
current = 0
for right, down in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
    for n in range(0, len(lines), down):
        a = (n // down * right) % length
        if lines[n][a] == "#":
            current += 1
    trees.append(current)
    current = 0

p1 = trees[1]
p2 = reduce((lambda x, y: x * y), trees)

print(p1)
print(p2)
