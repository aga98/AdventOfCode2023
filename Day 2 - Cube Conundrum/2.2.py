
def fill_game_color_dict(set_cube: str, color_dict: dict[str, list]):
    cubes = set_cube.split(",")
    for cube in cubes:
        cube = cube.strip()
        amount, color = cube.split(" ")
        color_dict[color].append(int(amount))


def get_game_mult(game: str) -> int:
    game_definition = game.split(":")[1].strip()
    sets = game_definition.split(";")
    cube_color_amounts = {
        "red": [0],
        "green": [0],
        "blue": [0],
    }
    for s in sets:
        fill_game_color_dict(s.strip(), cube_color_amounts)
    return max(cube_color_amounts["red"]) * max(cube_color_amounts["green"]) * max(cube_color_amounts["blue"])


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        cube_games = f.readlines()

    min_cubes_mult_sum = sum(get_game_mult(g) for g in cube_games)
    print(min_cubes_mult_sum)

