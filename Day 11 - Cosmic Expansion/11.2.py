from utils import read_input
from common import process_input, calculate_pair_distances

EXPANDS = 1000000  # with 2, it would also solve part 1


def get_galaxies_coordinates(
        galaxies: dict[str, tuple[int, int]],
        rows_to_expand: list, 
        cols_to_expand: list
) -> dict[str, tuple[int, int]]:
    galaxies_coordinates = {}
    for i, row in enumerate(galaxies):
        for j, pixel in enumerate(row):
            if pixel != ".":
                num_rows_to_expand_before = sum(1 for row_to_expand in rows_to_expand if row_to_expand < i)
                num_cols_to_expand_before = sum(1 for col_to_expand in cols_to_expand if col_to_expand < j)
                new_i = i + num_rows_to_expand_before * (EXPANDS - 1)
                new_j = j + num_cols_to_expand_before * (EXPANDS - 1)
                galaxies_coordinates[pixel] = (new_i, new_j)
    return galaxies_coordinates


if __name__ == "__main__":
    image, expand_rows, expand_cols = process_input(read_input())
    coordinates = get_galaxies_coordinates(image, expand_rows, expand_cols)
    distances = calculate_pair_distances(coordinates)
    distances_sum = sum(sum(distances[galaxy].values()) for galaxy in distances)
    print(f"Sum of distances: {int(distances_sum / 2)}")  # divide by 2 because we are counting each pair twice
