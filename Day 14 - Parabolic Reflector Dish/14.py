from typing import List, Tuple

from utils import read_input


DIRECTIONS = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0),
}

def process_input(lines: list[str]) -> list[list[str]]:
    return [list(line) for line in lines]


def move_rock(platform: list[list[str]], rock: tuple[int, int], direction: str) -> tuple[int, int]:
    """
    Move a rock in a given direction, until it hits another rock or the edge
    """
    row, col = rock
    while True:
        row += DIRECTIONS[direction][0]
        col += DIRECTIONS[direction][1]
        # check edges
        if row < 0 or row >= len(platform) or col < 0 or col >= len(platform[0]):
            return row - DIRECTIONS[direction][0], col - DIRECTIONS[direction][1]
        if platform[row][col] in ["O", "#"]:
            return row - DIRECTIONS[direction][0], col - DIRECTIONS[direction][1]
            

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


def calculate_load(locations: list[tuple[int, int]], num_rows: int) -> int:
    """
    Calculate the load of the dish, given the locations of the rocks
    """
    print(locations)
    load = 0
    for i, j in locations:
        load += num_rows - i
    return load


if __name__ == "__main__":
    plat = process_input(read_input())
    locs = tilt(plat, "up")
    total_load = calculate_load(locs, len(plat))
    print(f"Total load: {total_load}")
