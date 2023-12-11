def process_input(img: list[list[str]]) -> (list[list[str]], list[int], list[int]):
    rows_galaxies = [0]*len(img)
    cols_galaxies = [0]*len(img[0])
    galaxy_id = 0
    galaxies = [["."]*(len(img[0])) for _ in range(len(img))]
    for i, point in enumerate(img):
        for j, pixel in enumerate(point):
            if pixel == "#":
                rows_galaxies[i] += 1
                cols_galaxies[j] += 1
                galaxies[i][j] = str(galaxy_id)
                galaxy_id += 1

    rows_to_expand = [i for i, num_galaxies in enumerate(rows_galaxies) if num_galaxies == 0]
    cols_to_expand = [i for i, num_galaxies in enumerate(cols_galaxies) if num_galaxies == 0]
    return galaxies, rows_to_expand, cols_to_expand


def calculate_pair_distances(
        galaxies: list[list[str]], galaxy_coordinates: dict[str, list[tuple[int, int]]]
) -> dict[str, dict[str, int]]:
    pair_distances = {}
    for galaxy, coordinates in galaxy_coordinates.items():
        pair_distances[galaxy] = {}
        for other_galaxy, other_coordinates in galaxy_coordinates.items():
            if galaxy != other_galaxy:
                pair_distances[galaxy][other_galaxy] = min(
                    abs(x1 - x2) + abs(y1 - y2)
                    for x1, y1 in coordinates
                    for x2, y2 in other_coordinates
                )
    return pair_distances
