from get_input import get_input

puzzle_input = get_input(filename=__file__, split_lines=True, strip=False)


stack_idx = []
p1_stacks = []
for row in puzzle_input[: puzzle_input.index("")][::-1]:
    if not stack_idx:
        stack_idx = tuple(idx for idx, char in enumerate(row) if char.isdigit())
        p1_stacks = [[] for _ in range(len(stack_idx))]
    else:
        for n, idx in enumerate(stack_idx):
            if (char := row[idx]) != " ":
                p1_stacks[n].append(char)


p2_stacks = [s[:] for s in p1_stacks]
for move in puzzle_input[puzzle_input.index("") :]:
    if not move:
        continue
    number, s1, s2 = [int(v) for n, v in enumerate(move.split()) if n in (1, 3, 5)]
    s1 -= 1
    s2 -= 1
    p1_stacks[s2].extend(p1_stacks[s1][-number:][::-1])
    p1_stacks[s1] = p1_stacks[s1][:-number]
    p2_stacks[s2].extend(p2_stacks[s1][-number:])
    p2_stacks[s1] = p2_stacks[s1][:-number]

p1 = "".join([stack[-1] for stack in p1_stacks])
p2 = "".join([stack[-1] for stack in p2_stacks])

print(p1)
print(p2)
