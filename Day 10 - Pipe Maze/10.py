from utils import read_input

"""
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is the starting position of the animal; there is a pipe on this tile,
    but your sketch doesn't show what shape the pipe has.
"""
from collections import defaultdict

MAZE_SYMBOLS = {"|", "-", "L", "J", "7", "F", "S"}


class Graph:
    def __init__(self, matrix: list[list[str]]):
        self.nodes = defaultdict(set)
        self.matrix = matrix
        self.start = None
        self.read_graph()

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes[node] = set()

    def add_edge(self, node1, node2):
        self.nodes[node1].add(node2)

    def _add_up_edges(self, i, j):
        if i > 0 and self.matrix[i - 1][j] in MAZE_SYMBOLS:
            self.add_edge((i, j), (i - 1, j))

    def _add_down_edges(self, i, j):
        if i < len(self.matrix) - 1 and self.matrix[i + 1][j] in MAZE_SYMBOLS:
            self.add_edge((i, j), (i + 1, j))

    def _add_left_edges(self, i, j):
        if j > 0 and self.matrix[i][j - 1] in MAZE_SYMBOLS:
            self.add_edge((i, j), (i, j - 1))

    def _add_right_edges(self, i, j):
        if j < len(self.matrix[0]) - 1 and self.matrix[i][j + 1] in MAZE_SYMBOLS:
            self.add_edge((i, j), (i, j + 1))

    def _replace_start(self, i, j) -> str:
        # replace with "-"
        if (
                0 < j < len(self.matrix[0]) - 1
                and self.matrix[i][j - 1] in ["-", "F", "L"]
                and self.matrix[i][j + 1] in ["-", "J", "7"]
        ):
            return "-"
        # replace with "|"
        elif (
                0 < i < len(self.matrix) - 1
                and self.matrix[i - 1][j] in ["|", "7", "F"]
                and self.matrix[i + 1][j] in ["|", "L", "J"]
        ):
            return "|"
        # replace with "L"
        elif (
                0 < i < len(self.matrix) - 1
                and j < len(self.matrix[0]) - 1
                and self.matrix[i - 1][j] in ["|", "7", "F"]
                and self.matrix[i][j + 1] in ["-", "J", "7"]
        ):
            return "L"
        # replace with "J"
        elif (
                0 < i < len(self.matrix) - 1
                and j > 0
                and self.matrix[i - 1][j] in ["|", "7", "F"]
                and self.matrix[i][j - 1] in ["-", "F", "L"]
        ):
            return "J"
        # replace with "7"
        elif (
                i < len(self.matrix) - 1
                and j > 0
                and self.matrix[i + 1][j] in ["|", "L", "J"]
                and self.matrix[i][j - 1] in ["-", "F", "L"]
        ):
            return "7"
        # replace with "F"
        elif (
                i < len(self.matrix) - 1
                and j < len(self.matrix[0]) - 1
                and self.matrix[i + 1][j] in ["|", "L", "J"]
                and self.matrix[i][j + 1] in ["-", "J", "7"]
        ):
            return "F"
        else:
            raise ValueError(f"Invalid start position: {i, j}")

    def read_graph(self):
        for i, row in enumerate(self.matrix):
            for j, tile in enumerate(row):
                if tile in MAZE_SYMBOLS:
                    if tile == "S":  # replace start with right symbol
                        self.start = (i, j)
                        tile = self._replace_start(i, j)
                    self.add_node((i, j))
                    if tile == "|":
                        self._add_up_edges(i, j)
                        self._add_down_edges(i, j)
                    elif tile == "-":
                        self._add_left_edges(i, j)
                        self._add_right_edges(i, j)
                    elif tile == "L":
                        self._add_up_edges(i, j)
                        self._add_right_edges(i, j)
                    elif tile == "J":
                        self._add_up_edges(i, j)
                        self._add_left_edges(i, j)
                    elif tile == "7":
                        self._add_down_edges(i, j)
                        self._add_left_edges(i, j)
                    elif tile == "F":
                        self._add_down_edges(i, j)
                        self._add_right_edges(i, j)

    def bfs(self):
        start = self.start
        visited = set()
        queue = [start]
        distances = {start: 0}
        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                for neighbour in self.nodes[node]:
                    if neighbour not in visited:
                        queue.append(neighbour)
                        distances[neighbour] = distances[node] + 1
        return distances

    def print_distances(self, distances):
        for i, row in enumerate(self.matrix):
            for j, tile in enumerate(row):
                if tile in MAZE_SYMBOLS:
                    print(distances.get((i, j), "."), end="")
                else:
                    print(tile, end="")
            print()


# Part 2
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
    inside = area - boundary / 2 + 1
    print(f"Area: {area}, Boundary: {boundary} --> Inside: {inside}")


if __name__ == "__main__":
    maze = read_input()
    g = Graph(maze)
    dists = g.bfs()
    # g.print_distances(dists)
    max_dist = max(dists.values())
    print(f"Max distance: {max_dist}")

    loop_points_bfs = list(dists.keys())  # not in order because of BFS
    loop_points_even = loop_points_bfs[::2]
    loop_points_odd = loop_points_bfs[1::2][::-1]  # reverse the order
    loop = loop_points_even + loop_points_odd
    calculate_inside_points(loop)
