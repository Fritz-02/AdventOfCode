from get_input import get_input

puzzle_input = get_input(filename=__file__, split_lines=True)


p1 = 0
p2 = 0
for idx in range(len(puzzle_input)):
    seq = [
        [int(n) for n in puzzle_input[idx].split()],
    ]
    while any(seq[-1]):
        seq.append([seq[-1][n] - seq[-1][n - 1] for n in range(1, len(seq[-1]))])
    seq[-1] = [0, *seq[-1], 0]
    seq.reverse()
    for n in range(1, len(seq)):
        prev_seq = seq[n - 1]
        curr_seq = seq[n]
        seq[n] = [curr_seq[0] - prev_seq[0], *seq[n], curr_seq[-1] + prev_seq[-1]]
    p1 += seq[-1][-1]
    p2 += seq[-1][0]

print(p1)
print(p2)
