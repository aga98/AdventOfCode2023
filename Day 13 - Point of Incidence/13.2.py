from utils import read_input
from common import process_input, check_reflections


def get_reflection_line(valley: list[str], expected_diff: int = 0) -> int | None:
    for index, row in enumerate(valley[:-1]):
        row2 = valley[index + 1]
        matching_chars = [False] * len(row)
        for i in range(len(row)):
            matching_chars[i] = row[i] == row2[i]
        if matching_chars.count(False) == expected_diff:
            return index
    return None


def find_reflections(valley: list[str]) -> int:
    result = 0
    transposed_valley = ["".join(row) for row in list(map(list, zip(*valley)))]
    horizontal_reflection_line = get_reflection_line(valley, expected_diff=1)
    vertical_reflection_line = get_reflection_line(transposed_valley, expected_diff=1)
    if horizontal_reflection_line is not None:
        result += 100 * (horizontal_reflection_line + 1)

    if vertical_reflection_line is not None:
        result += vertical_reflection_line + 1

    return result



if __name__ == "__main__":
    valleys = process_input(read_input(load_dummy=True))
    reflection_number = 0
    for val_i, val in enumerate(valleys):
        reflections = find_reflections(val)
        print(f"Reflection calculation for valley {val_i}: {reflections}")
        reflection_number += reflections
    print(f"Total reflection calculation: {reflection_number}")
