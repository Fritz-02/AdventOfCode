from get_input import get_input

puzzle_input = get_input(2022, 2)


p1 = 0
p2 = 0
opponent = ("A", "B", "C")
you = ("X", "Y", "Z")
for a, b in [r.split() for r in puzzle_input.split("\n")]:
    a = opponent.index(a)
    b = you.index(b)
    hand = ((a + 2) % 3, a, (a + 1) % 3)
    p1 += hand.index(b) * 3 + b + 1
    p2 += b * 3 + hand[b] + 1

print(p1)
print(p2)
