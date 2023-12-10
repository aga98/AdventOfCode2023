from utils import read_input


def calculate_number_of_matches(winner_numbers: list, card_numbers: list) -> int:
    return sum(1 for num in card_numbers if num in winner_numbers)


def matches_2_points(matches: int) -> int:
    points = 0
    point_value = 1
    for i in range(matches):
        if i == 2:
            point_value += 1
        elif i >= 3:
            point_value *= 2
        points += point_value
    return points


def get_scratchcard_points(card: str) -> int:
    card = card.split(":")[1].strip()
    winner_numbers = [int(num.strip()) for num in card.split("|")[0].strip().split()]
    card_numbers = [int(num.strip()) for num in card.split("|")[1].strip().split()]
    matches = calculate_number_of_matches(winner_numbers, card_numbers)
    points = matches_2_points(matches)
    print(f"{winner_numbers} | {card_numbers} --> {points} points ({matches} matches)")
    return points


if __name__ == "__main__":
    scratchcards = read_input()
    pile_points = sum(get_scratchcard_points(c) for c in scratchcards)
    print(pile_points)
