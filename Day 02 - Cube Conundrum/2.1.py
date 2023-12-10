import re
from utils import read_input


color_amounts = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def validate_set(set_cube: str) -> bool:
    cubes = set_cube.split(",")
    for cube in cubes:
        cube = cube.strip()
        amount, color = cube.split(" ")
        if int(amount) > color_amounts[color]:
            return False
    return True


def get_game_id_if_valid(game: str) -> int:
    game_number = re.search("Game (.+?):", game)[1]
    game_definition = game.split(":")[1].strip()
    sets = game_definition.split(";")
    for s in sets:
        if not validate_set(s.strip()):
            return 0
    return int(game_number)


if __name__ == "__main__":
    cube_games = read_input()
    id_sum = sum(get_game_id_if_valid(g) for g in cube_games)
    print(id_sum)


