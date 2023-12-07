from get_input import get_input

hands = get_input(filename=__file__, split_lines=True)


def card_to_integer(card: str) -> int:
    return int(card) if card.isdigit() else ("T", "J", "Q", "K", "A").index(card) + 10


def convert_cards(cards: str, joker: bool = False) -> tuple[int, tuple[int, ...]]:
    card_set = set(cards)
    joker_count = 0
    if joker and "J" in card_set:
        joker_count = cards.count("J")
        card_set.remove("J")
        if joker_count == 5:
            card_set = {"A"}

    card_count = list(
        sorted(((cards.count(char), char) for char in card_set), reverse=True)
    )
    card_count[0] = (card_count[0][0] + joker_count, card_count[0][1])
    card_ints = tuple(
        card_to_integer(char)
        for char in (cards if not joker else cards.replace("J", "1"))
    )

    if (q := len(card_set)) == 5:
        return 0, card_ints
    elif q == 4:
        return 1, card_ints
    elif q == 1:
        return 6, card_ints
    elif q == 3:
        return 2 + (card_count[0][0] == 3), card_ints
    elif q == 2:
        return 4 + (card_count[0][0] == 4), card_ints


p1_ranks = []
p2_ranks = []
winnings = 0
for hand in hands:
    c, bid = hand.split()
    p1_ranks.append((convert_cards(c), int(bid)))
    p2_ranks.append((convert_cards(c, True), int(bid)))

p1_ranks.sort()
p2_ranks.sort()

p1 = 0
for n, (_, bid) in enumerate(p1_ranks):
    p1 += (n + 1) * bid

p2 = 0
for n, (_, bid) in enumerate(p2_ranks):
    p2 += (n + 1) * bid

print(p1)
print(p2)
