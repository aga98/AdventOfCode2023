import re


def line_to_list(line, same_line: bool = False) -> list:
    if same_line:
        return [int(num) for num in line.replace("\n", "").split(":")[1].strip().split(" ")]
    else:
        return [int(num) for num in line.replace("\n", "").strip().split(" ")]


def read_input():
    with open("./input_dummy.txt", "r") as f:
        lines = f.readlines()

    input_dict = {}
    seeds = []
    current_map = None
    for line in lines:
        if line.startswith("seeds:"):
            seeds = line_to_list(line, same_line=True)
        elif re.match(r"^[a-zA-Z]", line):
            current_map = line.split()[0]
            input_dict[current_map] = []
        elif re.match(r"^\d", line):
            input_dict[current_map].append(line_to_list(line))

    return seeds, input_dict


def source_to_destination(value: int, mapping_list: list):
    for map_dest, map_source, length in mapping_list:
        if map_source <= value <= map_source + length:
            offset = value - map_source
            return map_dest + offset
    return value


def seed_to_location(seed: int, mappings: dict):
    soil = source_to_destination(seed, mappings["seed-to-soil"])
    fertilizer = source_to_destination(soil, mappings["soil-to-fertilizer"])
    water = source_to_destination(fertilizer, mappings["fertilizer-to-water"])
    light = source_to_destination(water, mappings["water-to-light"])
    temperature = source_to_destination(light, mappings["light-to-temperature"])
    humidity = source_to_destination(temperature, mappings["temperature-to-humidity"])
    location = source_to_destination(humidity, mappings["humidity-to-location"])
    print(f"Seed {seed} --> Soil {soil} --> Fertilizer {fertilizer} --> Water {water} --> Light {light} "
          f"--> Temperature {temperature} --> Humidity {humidity} --> Location {location}")
    return location


if __name__ == "__main__":
    seed_list, input_map = read_input()
    locations = [seed_to_location(s, input_map) for s in seed_list]
    min_location = min(locations)
    print(f"Min location: {min_location}")

