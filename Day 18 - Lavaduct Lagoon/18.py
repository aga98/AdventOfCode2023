from typing import Tuple, List, Set

from utils import read_input


DIRECTIONS = {
    "U": (-1, 0),
    "D": (1, 0),
    "R": (0, 1),
    "L": (0, -1),
}


def process_input(lines: list[str]) -> list[tuple[str, int, str]]:
    instructions = []
    for line in lines:
        splitted = line.split(" ")
        direction = splitted[0]
        distance = int(splitted[1])
        color = splitted[2].replace("(", "").replace(")", "")
        instructions.append((direction, distance, color))
    return instructions


def print_matrix(matrix: list[list[str]]):
    for row in matrix:
        print(" ".join(row))
    print()


def build_matrix(dug: set[tuple[int, int]]):
    iss = [i for i, _ in dug]
    min_row, max_row = min(iss), max(iss)
    jss = [j for _, j in dug]
    min_col, max_col = min(jss), max(jss)
    final_dug_matrix = [["."] * (max_col - min_col + 1) for _ in range(max_row - min_row + 1)]
    for i, j in dug:
        new_i = i - min_row
        new_j = j - min_col
        final_dug_matrix[new_i][new_j] = "#"
    return final_dug_matrix

    
def dig_edge(instructions: list[tuple[str, int, str]]) -> list[list[str]]:
    pos = (0, 0)
    dug = {pos}
    for direction, meters, _ in instructions:
        new_pos = pos
        for i in range(1, meters + 1):
            new_pos = (pos[0] + i * DIRECTIONS[direction][0], pos[1] + i * DIRECTIONS[direction][1])
            if new_pos not in dug:
                dug.add(new_pos)
        pos = new_pos
    matrix = build_matrix(dug)
    print_matrix(matrix)
    return matrix

    
def dig_inside(matrix):
    original_matrix = matrix.copy()
    cubes = set()
    for i in range(len(matrix)):
        crosses = 0
        for j in range(len(matrix[0])):
            previous_elems = matrix[i][j-2:j+1]
            # check left border

            if j == 0 and original_matrix[i][j] == "#" or original_matrix[i][j] == "#" and original_matrix[i][j - 1] != "#":
                crosses += 1
                cubes.add((i, j))

            elif j > 1 and original_matrix[i][j-2]:
                crosses += 1

            if crosses % 2 == 1:  # crossed an odd number of times -> inside
                matrix[i][j] = "#"
                cubes.add((i, j))

    print_matrix(matrix)
    return cubes


if __name__ == "__main__":
    plan = process_input(read_input(load_dummy=False))
    m = dig_edge(plan)
    total_cubes = dig_inside(m)
    print("Total cubes:", len(total_cubes))

