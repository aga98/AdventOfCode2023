from utils import read_input
from common import process_input, calculate_load, check_for_rock_and_move


DEBUG = False


def tilt(platform: list[list[str]], direction: str) -> list[tuple[int, int]]:
    cols = len(platform[0])
    rows = len(platform)
    locations = []
    if direction in ["left", "up"]:
        for i in range(rows):
            for j in range(cols):
                check_for_rock_and_move(platform, i, j, direction)
    else:
        for i in range(rows-1, -1, -1):
            for j in range(cols-1, -1, -1):
                check_for_rock_and_move(platform, i, j, direction)
     
    # store rock locations
    for i in range(rows):
        for j in range(cols):
            if platform[i][j] == "O":
                locations.append((i, j))
    
    if DEBUG:
        print(f"Tilted {direction}")
        for row in platform:
            print(row)
        
    return locations


def generate_loop(locations_history: list[list[tuple[int, int]]], index: int, cycles: int) -> list[tuple[int, int]]:
    loop = locations_history[index:]
    loop_length = len(loop) + 1
    index_final_location = loop_length - (cycles % loop_length + index % loop_length) - 1
    return loop[index_final_location]

    
def cycle(cycles: int, platform: list[list[str]]) -> list[tuple[int, int]]:
    sequence = ["up", "left", "down", "right"]
    locations_history = []
    locations = None
    moving = True
    i = 0
    while moving and i < cycles:
        for direction in sequence:
            locations = tilt(platform, direction)
            
        if locations in locations_history:
            moving = False
        else:
            locations_history.append(locations)
        i += 1
       
    if moving:
        return locations
    
    loop_start = locations_history.index(locations)
    return generate_loop(locations_history, loop_start, cycles)
    
    
if __name__ == "__main__":
    plat = process_input(read_input(load_dummy=False))
    locs = cycle(cycles=1000000000, platform=plat)
    total_load = calculate_load(locs, len(plat))
    print(f"Total load: {total_load}")
