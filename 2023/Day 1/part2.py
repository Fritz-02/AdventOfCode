import re

with open("input.txt") as f:
    puzzle_input = f.read()


num_strings = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
regex = re.compile(rf"(?=({'|'.join(num_strings)}|\d))")

answer = 0
for line in puzzle_input.split("\n"):
    digits = [
        (match if match.isdigit() else str(num_strings.index(match) + 1))
        for match in regex.findall(line)
    ]
    answer += int(digits[0] + digits[-1])

print(answer)
