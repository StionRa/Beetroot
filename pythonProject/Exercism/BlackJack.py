def value_of_card(card: str) -> int:
    if card in "JQK":
        return 10
    if card == "A":
        return 1
    return int(card)


def card_values(card_one: str, card_two: str) -> [int, int]:

    return value_of_card(card_one), value_of_card(card_two)


def higher_card(card_one: str, card_two: str) -> [str, str]:

    value_card_one, value_card_two = card_values(card_one, card_two)
    if value_card_one == value_card_two:
        return card_one, card_two
    if value_card_one > value_card_two:
        return card_one
    return card_two


def value_of_ace(card_one: str, card_two: str) -> int:

    return 11 if sum(card_values(card_one, card_two)) + (10 if 'A' in (card_one, card_two) else 0) <= 10 else 1
    #return 11 if sum(card_values(card_one, card_two)) <= 10 else 1
print(value_of_ace('A', '2'))
def is_blackjack(card_one: str, card_two: str) -> bool:

    return "A" in (card_one, card_two) and 10 in card_values(card_one, card_two)

def can_split_pairs(card_one: str, card_two: str) -> bool:

    value_cards = card_values(card_one, card_two)
    return value_cards[0] == value_cards[1]

def can_double_down(card_one: str, card_two: str) -> bool:

    return 9 <= sum(card_values(card_one, card_two)) <= 11