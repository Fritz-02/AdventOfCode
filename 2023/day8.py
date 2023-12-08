from get_input import get_input
import math

puzzle_input = get_input(filename=__file__, split_lines=True)


instructions = puzzle_input[0]
branches = {line[:3]: (line[7:10], line[12:15]) for line in puzzle_input[2:]}

p1_node = "AAA"
p2_nodes = [n for n in branches if n[2] == "A"]
p2_nodes_steps = []
step = 0
p1 = 0
while p1_node != "ZZZ" or p2_nodes:
    branch_direction = int(instructions[step % len(instructions)] == "R")
    step += 1
    if p1_node != "ZZZ":
        p1_node = branches[p1_node][branch_direction]
        p1 += 1
    if p2_nodes:
        p2_next = []
        for node in p2_nodes:
            if (next_node := branches[node][branch_direction])[2] == "Z":
                p2_nodes_steps.append(step)
            else:
                p2_next.append(next_node)
        p2_nodes = p2_next[:]

p2 = math.lcm(*p2_nodes_steps)

print(p1)
print(p2)
