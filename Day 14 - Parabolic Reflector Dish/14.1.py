from utils import read_input
from common import process_input, move_rock, calculate_load

DEBUG = True


def tilt(platform: list[list[str]], direction: str) -> list[tuple[int, int]]:
    cols = len(platform[0])
    rows = len(platform)
    locations = []
    for i in range(rows):
        for j in range(cols):
            if platform[i][j] == "O":  # move until we find a rock, or the edge
                new_row, new_col = move_rock(platform, (i, j), direction)
                if new_row != i or new_col != j:
                    platform[new_row][new_col] = "O"
                    platform[i][j] = "."
    
    # store rock locations
    for i in range(rows):
        for j in range(cols):
            if platform[i][j] == "O":
                locations.append((i, j))
    
    for row in platform:
        print(row)
    
    return locations


if __name__ == "__main__":
    plat = process_input(read_input(load_dummy=True))
    locs = tilt(plat, "up")
    total_load = calculate_load(locs, len(plat))
    print(f"Total load: {total_load}")

