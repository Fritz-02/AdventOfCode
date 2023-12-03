from get_input import get_input

puzzle_input = get_input(2020, 1)


p1 = 0
p2 = 0
entries = [int(entry) for entry in puzzle_input.split("\n")]
need_set = set()
need_triple = dict()
for x in range(len(entries)):
    entry = entries[x]
    if not p1:
        other = 2020 - entry
        if entry in need_set:
            p1 = entry * other
        elif other > 0:
            need_set.add(other)
    if not p2:
        if entry in need_triple:
            other_entries = need_triple[entry]
            p2 = entry * other_entries[0] * other_entries[1]
            continue
        for y in range(x + 1, len(entries)):
            other_entry = entries[y]
            if (entry + other_entry) < 2020:
                need_triple[2020 - entry - other_entry] = (entry, other_entry)
    if p1 and p2:
        break

print(p1)
print(p2)
