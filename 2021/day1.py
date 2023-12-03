from get_input import get_input

puzzle_input = get_input(2021, 1)


depths = [int(d) for d in puzzle_input.split("\n")]
p1 = sum((depths[n] > depths[n - 1]) for n in range(1, len(depths)))
p2 = sum(
    sum(depths[n - 2 : n + 1]) > sum(depths[n - 3 : n]) for n in range(3, len(depths))
)

print(p1)
print(p2)
