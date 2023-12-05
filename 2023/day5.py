from get_input import get_input


almanac = get_input(2023, 5).split("\n")


seeds = [int(seed) for seed in almanac[0].split(":")[1].split()]

values = seeds[:]
converted_values = []

pairs = [(seeds[i], seeds[i] + seeds[i + 1] - 1) for i in range(0, len(seeds), 2)]
converted_pairs = []

for line in almanac[1:]:
    if not line:
        continue
    if not line[0].isdigit():
        values = converted_values[:] + values
        converted_values = []
        pairs = converted_pairs[:] + pairs
        converted_pairs = []
    else:
        destination_start, source_start, range_length = (int(v) for v in line.split())
        source_end = source_start + range_length

        values_not_in_range = []
        while values:
            value = values.pop()
            if source_start <= value <= source_end:
                converted_values.append(value - source_start + destination_start)
            else:
                values_not_in_range.append(value)
        values = values_not_in_range[:]

        pairs_not_in_range = []
        while pairs:
            start, end = pairs.pop()
            before = (start, min(source_start, end))
            in_range = (max(start, source_start), min(source_end, end))
            after = (max(source_end, start), end)

            if before[1] > before[0]:
                pairs_not_in_range.append(before)
            if in_range[1] > in_range[0]:
                converted_pairs.append(
                    (
                        in_range[0] - source_start + destination_start,
                        in_range[1] - source_start + destination_start,
                    )
                )
            if after[1] > after[0]:
                pairs_not_in_range.append(after)
        pairs = pairs_not_in_range[:]

p1 = min(converted_values + values)
p2 = min([n[0] for n in converted_pairs + pairs])

print(p1)
print(p2)
