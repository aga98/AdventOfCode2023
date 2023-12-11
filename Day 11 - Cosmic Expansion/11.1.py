from utils import read_input
from common import process_input, calculate_pair_distances


def expand_galaxies(galaxies: list[list[str]], rows_to_expand: list, cols_to_expand: list) -> list[list[str]]:
    for expanded_rows, index_row in enumerate(rows_to_expand):
        galaxies.insert(index_row + expanded_rows, ["."]*len(galaxies[0]))

    for expanded_cols, index_col in enumerate(cols_to_expand):
        for galaxy in galaxies:
            galaxy.insert(index_col + expanded_cols, ".")

    return galaxies


def get_galaxies_coordinates(galaxies: list[list[str]]) -> dict[str, list[tuple[int, int]]]:
    galaxies_coordinates = {}
    for i, row in enumerate(galaxies):
        for j, pixel in enumerate(row):
            if pixel != ".":
                if pixel not in galaxies_coordinates:
                    galaxies_coordinates[pixel] = []
                galaxies_coordinates[pixel].append((i, j))
    return galaxies_coordinates


if __name__ == "__main__":
    image, expand_rows, expand_cols = process_input(read_input(load_dummy=False))
    image = expand_galaxies(image, expand_rows, expand_cols)
    coordinates = get_galaxies_coordinates(image)
    distances = calculate_pair_distances(image, coordinates)
    distances_sum = sum(sum(distances[galaxy].values()) for galaxy in distances)
    print(f"Sum of distances: {int(distances_sum / 2)}")  # divide by 2 because we are counting each pair twice
