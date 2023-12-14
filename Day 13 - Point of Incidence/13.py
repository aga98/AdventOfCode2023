from utils import read_input
from common import process_input, check_reflections


def get_reflection_line(valley: list[str]) -> int | None:
    counts = {}
    for index, row in enumerate(valley):
        if row in counts:
            counts[row].append(index)
        else:
            counts[row] = [index]

    # the line will be the row where the count has at least two elements and contains i and i+1
    reflection_candidates = [row for row in counts if len(counts[row]) >= 2]
    for row in reflection_candidates:
        for i in range(len(counts[row]) - 1):
            if counts[row][i] + 1 == counts[row][i + 1] and check_reflections(counts[row][i], valley):
                return counts[row][i]
    return None


def find_reflections(valley: list[str]) -> int:
    result = 0
    transposed_valley = ["".join(row) for row in list(map(list, zip(*valley)))]

    horizontal_reflection_line = get_reflection_line(valley)
    vertical_reflection_line = get_reflection_line(transposed_valley)

    if horizontal_reflection_line is not None:
        result += 100 * (horizontal_reflection_line + 1)

    if vertical_reflection_line is not None:
        result += vertical_reflection_line + 1

    return result


if __name__ == "__main__":
    valleys = process_input(read_input(load_dummy=False))
    reflection_number = 0
    for val_i, val in enumerate(valleys):
        reflections = find_reflections(val)
        print(f"Reflection calculation for valley {val_i}: {reflections}")
        reflection_number += reflections
    print(f"Total reflection calculation: {reflection_number}")

