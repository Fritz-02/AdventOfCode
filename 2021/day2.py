from get_input import get_input

puzzle_input = get_input(2021, 2)


pos = 0
depth_aim = 0
depth2 = 0
for direction, value in (cmd.split() for cmd in puzzle_input.split("\n")):
    value = int(value)
    if direction == "up":
        depth_aim -= value
    elif direction == "down":
        depth_aim += value
    elif direction == "forward":
        pos += value
        depth2 += depth_aim * value

p1 = pos * depth_aim
p2 = pos * depth2

print(p1)
print(p2)
