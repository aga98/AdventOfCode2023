def process_input(lines: list) -> list:
    lines = [line.split() for line in lines]
    return [[int(value) for value in line] for line in lines]
