from get_input import get_input

puzzle_input = get_input(2021, 3)


data = [int(line, 2) for line in puzzle_input.split("\n")]
most_common_bits = [
    str(sum((x & (1 << pos)) >> pos for x in data) > len(data) // 2)
    for pos in reversed(range(data[0].bit_length()))
]
gamma = int("".join(most_common_bits), 2)
epsilon = int("".join([str(int(bit) ^ 1) for bit in most_common_bits]), 2)
p1 = gamma * epsilon

oxygen = data[:]
pos = oxygen[0].bit_length() - 1
while len(oxygen) > 1:
    if sum((x & (1 << pos)) >> pos for x in oxygen) >= (len(oxygen) / 2):
        oxygen = [x for x in oxygen if x & (1 << pos)]
    else:
        oxygen = [x for x in oxygen if not x & (1 << pos)]
    pos -= 1

co2 = data[:]
pos = co2[0].bit_length() - 1
while len(co2) > 1:
    if sum((x & (1 << pos)) >> pos for x in co2) < (len(co2) / 2):
        co2 = [x for x in co2 if x & (1 << pos)]
    else:
        co2 = [x for x in co2 if not x & (1 << pos)]
    pos -= 1

p2 = oxygen[0] * co2[0]

print(p1)
print(p2)
