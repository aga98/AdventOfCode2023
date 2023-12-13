from utils import read_input


def process_input(lines: list[str]) -> list[list[str]]:
    valley_list = [[]]
    num_valley = 0
    for line in lines:
        if line != "":
            valley_list[num_valley].append(line)
        else:
            valley_list.append([])
            num_valley += 1
    return valley_list


def check_reflections(reflection_line: int, valley: list[str]) -> int:
    """
    Validate it is actually a reflection line
    """
    l = reflection_line
    r = reflection_line + 1
    matches = 0
    while l >= 0 and r < len(valley):
        if valley[l] != valley[r]:
            return False
        matches += 1
        l -= 1
        r += 1
    return True


def get_reflection_line(valley: list[str]) -> int | None:
    counts = {}
    for index, row in enumerate(valley):
        if row in counts:
            counts[row].append(index)
        else:
            counts[row] = [index]

    # the diagonal will be the row where the count has at least two elements and contains i and i+1
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

