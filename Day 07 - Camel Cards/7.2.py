from collections import Counter
from utils import read_input
from common import get_hand_type, process_input

CARD_LIST = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]


class Card:
    def __init__(self, card: str):
        self.card = card
        self.rank = CARD_LIST.index(card)

    def __lt__(self, other):
        return self.rank < other.rank

    def __repr__(self):
        return self.card


class Hand:
    def __init__(self, cards: str, bid: str):
        self.cards = [Card(card) for card in cards]
        self.cards_replaced = self.replace_jokers_with_best_card()
        self.hand_value = get_hand_type([card.card for card in self.cards_replaced])
        self.bid = int(bid)

    def __lt__(self, other):
        if self.hand_value != other.hand_value:
            return self.hand_value.value < other.hand_value.value
        for card1, card2 in zip(self.cards, other.cards):
            if card1.card != card2.card:
                return card1.rank < card2.rank
            
    def __repr__(self):
        return "".join([card.card for card in self.cards])

    def replace_jokers_with_best_card(self) -> list:
        """
        Replaces Jokers with the best card in the hand
        Example: JJJJ2 -> 22222, 333J2 -> 33332, KJ987 -> KK987
        """
        cards = [card.card for card in self.cards]
        card_counts = Counter(cards).items()
        card_counts = sorted(card_counts, key=lambda x: (x[1], x[0]), reverse=True)
        if len(card_counts) == 1:
            return self.cards
        best_card = card_counts[0][0] if card_counts[0][0] != "J" else card_counts[1][0]
        cards_replaced = str(self).replace("J", best_card)
        return [Card(card) for card in cards_replaced]


if __name__ == "__main__":
    game = process_input(read_input())
    hands = [Hand(cards=game[0], bid=game[1]) for game in game]
    sorted_hands = sorted(hands)
    winnings = 0
    for rank, hand in enumerate(sorted_hands, start=1):
        winnings += hand.bid * rank
        print(f"Hand: {str(hand.cards)}, Replaced hand: {hand.cards_replaced}, "
              f"Type {hand.hand_value}, Bid: {hand.bid}, Rank: {rank}")
    print(f"Total winnings: {winnings}")
