import re


def calculate_number_of_matches(winner_numbers: list, card_numbers: list) -> int:
    return sum(1 for num in card_numbers if num in winner_numbers)


def get_number_of_scratchcards(scratchcard_amounts: dict, card: str):
    num_card = int(re.search("Card (.+?):", card)[1])
    card = card.split(":")[1].strip()
    winner_numbers = [int(num.strip()) for num in card.split("|")[0].strip().split()]
    card_numbers = [int(num.strip()) for num in card.split("|")[1].strip().split()]
    matches = calculate_number_of_matches(winner_numbers, card_numbers)
    for i in range(1, matches+1):
        if num_card+i in scratchcard_amounts:
            scratchcard_amounts[num_card+i] += scratchcard_amounts[num_card]


if __name__ == "__main__":
    with open("./input.txt", "r") as f:
        scratchcards = f.readlines()
        scratchcard_amounts = {k: 1 for k in range(1, len(scratchcards) + 1)}
        for scratchcard in scratchcards:
            get_number_of_scratchcards(scratchcard_amounts, scratchcard)
        total_scratchcards = sum(scratchcard_amounts.values())
        print(scratchcard_amounts)
        print(total_scratchcards)
