import re


def line_to_list(line, same_line: bool = False) -> list:
    if same_line:
        return [int(num) for num in line.replace("\n", "").split(":")[1].strip().split(" ")]
    else:
        return [int(num) for num in line.replace("\n", "").strip().split(" ")]


def read_input():
    with open("./input.txt", "r") as f:
        lines = f.readlines()

    input_dict = {}
    seeds = []
    current_map = None
    for line in lines:
        if line.startswith("seeds:"):
            seed_list = line_to_list(line, same_line=True)
            for i in range(0, len(seed_list), 2):
                seeds.append((seed_list[i], seed_list[i+1]))
        elif re.match(r"^[a-zA-Z]", line):
            current_map = line.split()[0]
            input_dict[current_map] = []
        elif re.match(r"^\d", line):
            input_dict[current_map].append(line_to_list(line))
    return seeds, input_dict


def destination_to_source(value: int, mapping_list: list):
    return next(
        (
            map_source + (value - map_dest)
            for map_dest, map_source, length in mapping_list
            if map_dest <= value <= map_dest + length
        ),
        value,
    )


def location_to_seed(location: int, mappings: dict):
    humidity = destination_to_source(location, mappings["humidity-to-location"])
    temperature = destination_to_source(humidity, mappings["temperature-to-humidity"])
    light = destination_to_source(temperature, mappings["light-to-temperature"])
    water = destination_to_source(light, mappings["water-to-light"])
    fertilizer = destination_to_source(water, mappings["fertilizer-to-water"])
    soil = destination_to_source(fertilizer, mappings["soil-to-fertilizer"])
    seed = destination_to_source(soil, mappings["seed-to-soil"])
    print(f"Location {location} --> Humidity {humidity} --> Temperature {temperature} --> Light {light} "
          f"--> Water {water} --> Fertilizer {fertilizer} --> Soil {soil} --> Seed {seed}")
    return seed


def have_seed(seed: int, seeds: list) -> bool:
    return any(interval[0] <= seed <= interval[0]+interval[1] for interval in seeds)


def find_seed_from_locations(mapping: dict, seeds: list):
    locations = mapping["humidity-to-location"]
    sorted_locations = sorted(locations, key=lambda x: x[0])
    for location_definition in sorted_locations:
        for location in range(location_definition[0], location_definition[0] + location_definition[2] + 1):
            seed = location_to_seed(location, mapping)
            if have_seed(seed, seeds):
                print(f"Seed {seed} found at location {location}")
                return location, seed


if __name__ == "__main__":
    seed_list, input_map = read_input()
    find_seed_from_locations(input_map, seed_list)
