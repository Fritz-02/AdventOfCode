from get_input import get_input

puzzle_input = get_input(2020, 2)


p1 = 0
p2 = 0
for policy, password, *q in (line.split(": ") for line in puzzle_input.split("\n")):
    nums, letter = policy.split()
    a, b = (int(n) for n in nums.split("-"))
    if a <= password.count(letter) <= b:
        p1 += 1
    if (password[a - 1], password[b - 1]).count(letter) == 1:
        p2 += 1

print(p1)
print(p2)
