from common import process_input, get_hand_type
from utils import read_input

CARD_LIST = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]


class Hand:
    def __init__(self, cards: str, bid: str):
        self.cards = cards
        self.hand_value = get_hand_type(cards)
        self.bid = int(bid)

    def __lt__(self, other):
        if self.hand_value != other.hand_value:
            return self.hand_value.value < other.hand_value.value
        for card1, card2 in zip(self.cards, other.cards):
            if card1 != card2:
                return CARD_LIST.index(card1) < CARD_LIST.index(card2)


if __name__ == "__main__":
    game = process_input(read_input())
    hands = [Hand(cards=game[0], bid=game[1]) for game in game]
    sorted_hands = sorted(hands)
    winnings = 0
    for rank, hand in enumerate(sorted_hands, start=1):
        winnings += hand.bid * rank
        print(f"Hand: {hand.cards}, Type {hand.hand_value}, Bid: {hand.bid}, Rank: {rank}")
    print(f"Total winnings: {winnings}")
