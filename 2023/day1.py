from get_input import get_input
import re

puzzle_input = get_input(2023, 1)


num_strings = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
regex = re.compile(rf"(?=({'|'.join(num_strings)}|\d))")

p1 = 0
p2 = 0
for line in puzzle_input.split("\n"):
    d1 = re.findall(r"\d", line)
    d2 = [
        (match if match.isdigit() else str(num_strings.index(match) + 1))
        for match in regex.findall(line)
    ]
    p1 += int(d1[0] + d1[-1])
    p2 += int(d2[0] + d2[-1])

print(p1)
print(p2)
