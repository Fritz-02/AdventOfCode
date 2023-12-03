from get_input import get_input
from functools import reduce

puzzle_input = get_input(2022, 3)


sacks = puzzle_input.split("\n")
p1 = 0
p2 = 0
for n in range(0, len(sacks), 3):
    sack_group = sacks[n : n + 3]
    for sack in sack_group:
        mid = len(sack) // 2
        comp1 = set(sack[:mid])
        comp2 = set(sack[mid:])
        for shared_item in comp1 & comp2:
            n = ord(shared_item)
            p1 += n - (96 if n > 96 else 38)
    badge = reduce(lambda x, y: x & y, (set(sack) for sack in sack_group))
    b = ord(badge.pop())
    p2 += b - (96 if b > 96 else 38)

print(p1)
print(p2)
