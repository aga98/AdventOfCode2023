def read_input(load_dummy: bool = False) -> list:
    filename = "input_dummy.txt" if load_dummy else "input.txt"
    with open(filename, "r") as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        if line.endswith("\n"):
            lines[i] = line[:-1]
    return lines
