from get_input import get_input

puzzle_input = get_input(2022, 1)


total_calories = sorted(
    [
        sum([int(cal) for cal in inventory.split("\n")])
        for inventory in puzzle_input.split("\n\n")
    ],
    reverse=True,
)

print(total_calories[0])
print(sum(total_calories[:3]))
