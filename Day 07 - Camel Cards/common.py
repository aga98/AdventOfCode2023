from collections import Counter
from enum import Enum


class HandType(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7


def process_input(lines: list) -> (list, list):
    return [(line.split()[0], line.split()[1]) for line in lines]


def get_hand_type(cards: list | str) -> HandType:
    card_counts = Counter(cards).items()
    card_counts = sorted(card_counts, key=lambda x: x[1], reverse=True)
    if len(card_counts) == 5:  # high card: [(card, 1), (card, 1), (card, 1), (card, 1), (card, 1)]
        return HandType.HIGH_CARD
    elif len(card_counts) == 4:  # one pair: [(card, 2), (card, 1), (card, 1), (card, 1)]
        return HandType.ONE_PAIR
    elif len(card_counts) == 3:
        if card_counts[0][1] == 2:  # two pair: [(card, 2), (card, 2), (card, 1)]
            return HandType.TWO_PAIR
        elif card_counts[0][1] == 3:  # three of a kind: [(card, 3), (card, 1), (card, 1)]
            return HandType.THREE_OF_A_KIND
    elif len(card_counts) == 2:
        if card_counts[0][1] == 4:  # four of a kind: [(card, 4), (card, 1)]
            return HandType.FOUR_OF_A_KIND
        elif card_counts[0][1] == 3:  # full house: [(card, 3), (card, 2)]
            return HandType.FULL_HOUSE
    elif len(card_counts) == 1:  # five of a kind: [(card, 5)]
        return HandType.FIVE_OF_A_KIND
    else:
        raise ValueError(f"Unknown hand type: {card_counts}")
