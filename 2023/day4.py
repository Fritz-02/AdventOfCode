from get_input import get_input

puzzle_input = get_input(2023, 4)


p1 = 0
p2 = 0
cards = puzzle_input.split("\n")
scorecards = [
    1,
] * len(cards)
for n, card in enumerate(cards):
    winning_numbers, my_numbers = [
        set(int(x) for x in n.split()) for n in card[card.index(":") + 1:].split("|")
    ]
    amount = scorecards.pop(0)
    p2 += amount
    if matching_numbers := winning_numbers & my_numbers:
        p1 += 2 ** (len(matching_numbers) - 1)
        for a in range(len(matching_numbers)):
            scorecards[a] += amount

print(p1)
print(p2)
