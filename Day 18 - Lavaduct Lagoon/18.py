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
    
    # simplify by adding a padding
    padding = 1
    final_dug_matrix = [["."] * (max_col - min_col + 1 + 2 * padding) for _ in range(max_row - min_row + 1 + 2 * padding)]
    for i, j in dug:
        new_i = i - min_row + 1
        new_j = j - min_col + 1
        final_dug_matrix[new_i][new_j] = "#"
    return final_dug_matrix

    
def dig_edge(instructions: list[tuple[str, int, str]]) -> list[tuple[int, int]]:
    pos = (0, 0)
    dug = [pos]
    for direction, meters, _ in instructions:
        new_pos = pos
        for i in range(1, meters + 1):
            new_pos = (pos[0] + i * DIRECTIONS[direction][0], pos[1] + i * DIRECTIONS[direction][1])
            if new_pos not in dug:
                dug.append(new_pos)
        pos = new_pos
    matrix = build_matrix(dug)
    print_matrix(matrix)
    return dug

    
def calculate_inside_points(loop_points: list[tuple[int, int]]):
    """
    Pick's theorem: Suppose that a polygon has integer coordinates for all of its vertices.
    Let i be the number of integer points interior to the polygon, and
    let b be the number of integer points on its boundary
    (including both vertices and points along the sides).
    Then the area A of this polygon is
    A = i + b/2 - 1  --> i = A - b/2 + 1

    We need to calculate the area of the polygon and the number of points on its boundary.
    The shoelace formula, also known as Gauss's area formula and the surveyor's formula,
    is a mathematical algorithm to determine the area of a simple polygon
    whose vertices are described by their Cartesian coordinates in the plane.
    There are multiple formulas, but we can use the following one:
    A = 1/2 * sum[i=0 to n-1] [y_i(x_i-1 - x_i+1)]
    """
    def calculate_polygon_area(points: list[tuple[int, int]]) -> float:
        """Shoelace formula A = 1/2 * sum[i=0 to n-1] [y_i(x_i-1 - x_i+1)]"""
        polygon_area = 0
        xs = [x for x, _ in points]
        ys = [y for _, y in points]
        for i in range(len(points)):
            polygon_area += (ys[i] * (xs[i - 1] - xs[(i + 1) % len(xs)]))
        return abs(polygon_area) / 2

    area = calculate_polygon_area(loop_points)
    boundary = len(loop_points)
    inside = int(area - boundary / 2 + 1)
    print(f"Area: {area}, Boundary: {boundary} --> Inside: {inside}")
    return inside + boundary


if __name__ == "__main__":
    plan = process_input(read_input(load_dummy=False))
    edge = dig_edge(plan)
    total_cubes = calculate_inside_points(edge)
    print("Total cubes:", total_cubes)

