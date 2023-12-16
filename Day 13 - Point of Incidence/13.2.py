from utils import read_input
from common import process_input


def get_distance(row1: str, row2: str) -> int:
    return sum(a != b for a, b in zip(row1, row2))


def get_reflection_line(block: list[str], distance_to_match: int) -> int:
    for idx in range(len(block)):
        if sum(get_distance(l, r) for l, r in zip(reversed(block[:idx]), block[idx:])) == distance_to_match:
            return idx


def find_reflections(valley: list[str]) -> int:
    if row := get_reflection_line(valley, 1):
        return 100 * row
    
    if col := get_reflection_line(list(zip(*valley)), 1):
        return col


if __name__ == "__main__":
    valleys = process_input(read_input(load_dummy=False))
    reflection_number = sum(find_reflections(block) for block in valleys)
    print(f"Total reflection calculation: {reflection_number}")
