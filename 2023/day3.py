from get_input import get_input
import re

puzzle_input = get_input(2023, 3)


lines = puzzle_input.split("\n")
symbol_regex = re.compile(r"[^0-9.]")
gears = {}
p1 = 0
for y in range(len(lines)):
    line = lines[y]
    for num in re.finditer(r"\d+", line):
        start, end = num.span()
        num_val = int(num.group())
        start = max(start - 1, 0)
        end = min(end + 1, len(line))
        adj_chars = "".join(
            lines[a][start:end] for a in (y - 1, y, y + 1) if 0 <= a < len(lines)
        )
        if symbol_regex.search(adj_chars) is not None:
            p1 += num_val
        for gear in re.finditer(r"\*", adj_chars):
            idx = gear.span()[0]
            length = end - start
            gear_pos = (
                idx // length + y + 1 * (y == len(lines)) - 1 * (y > 0),  # row
                (idx % length) + start,  # col
            )
            if gear_pos in gears:
                gears[gear_pos].append(num_val)
            else:
                gears[gear_pos] = [num_val]

p2 = 0
for nums in gears.values():
    if len(nums) == 2:
        p2 += nums[0] * nums[1]

print(p1)
print(p2)
