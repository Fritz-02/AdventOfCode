import re

with open("input.txt") as f:
    puzzle_input = f.read()


answer = 0
for line in puzzle_input.split("\n"):
    digits = re.findall(r"\d", line)
    answer += int(digits[0] + digits[-1])

print(answer)
