from get_input import get_input
import re

puzzle_input = get_input(2015, 5)


rule1 = re.compile(r"[aeiou]")
rule2 = re.compile(r"(\w)\1")
rule3 = re.compile(r"ab|cd|pq|xy")
rule4 = re.compile(r"(\w{2}).*\1")
rule5 = re.compile(r"(\w).\1")
p1 = 0
p2 = 0
for line in puzzle_input.split("\n"):
    if len(rule1.findall(line)) >= 3 and rule2.search(line) and not rule3.search(line):
        p1 += 1
    if rule4.search(line) and rule5.search(line):
        p2 += 1

print(p1)
print(p2)
