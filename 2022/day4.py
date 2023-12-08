from get_input import get_input

assignments = get_input(filename=__file__, split_lines=True)


p1 = 0
p2 = 0
for pair in assignments:
    s1, s2 = sorted(tuple(int(b) for b in a.split("-")) for a in pair.split(","))
    if ((s1[1] - s1[0]) >= (s2[1] - s2[0])) and s1[1] >= s2[1]:
        p1 += 1
    elif s1[0] == s2[0] and s1[1] <= s2[1]:
        p1 += 1

    if s1[0] <= s2[0] <= s1[1] or s1[0] <= s2[1] <= s1[1]:
        p2 += 1

print(p1)
print(p2)
