import re
from collections import defaultdict
from utils import read_input


def symbol_in_surroundings(matrix, row: int, col_start: int, col_end: int, number: str, gears: dict):
    upper_bottom_cols = range(max(0, col_start - 1), min(col_end + 2, len(matrix[row])))

    if col_start != 0 and matrix[row][col_start-1] == "*":
        gears[f"{row},{col_start-1}"].append(number)
    if col_end + 1 != len(matrix[row]) and matrix[row][col_end+1] == "*":
        gears[f"{row},{col_end+1}"].append(number)

    # check if symbol is in the upper or bottom row
    for j in upper_bottom_cols:
        if row != 0 and matrix[row-1][j] == "*":
            gears[f"{row-1},{j}"].append(number)
        if row != len(matrix) - 1 and matrix[row+1][j] == "*":
            gears[f"{row+1},{j}"].append(number)


def process_row(matrix: list, gears: dict, i: int):
    findings = re.finditer(r"\d+", "".join(matrix[i]))
    for match in findings:
        col_start = match.start()
        col_end = match.end() - 1
        number = match.group()
        symbol_in_surroundings(matrix, i, col_start, col_end, number, gears)


def process_matrix(matrix):
    gears = defaultdict(list)
    for i, row in enumerate(matrix):
        process_row(matrix, gears, i)
    result = sum(int(nums[0]) * int(nums[1]) for nums in gears.values() if len(nums) == 2)
    print(result)


if __name__ == "__main__":
    mat = read_input()
    process_matrix(mat)

