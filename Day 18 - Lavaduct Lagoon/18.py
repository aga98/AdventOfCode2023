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


def print_digs(digged: set):
    iss = [i for i, _ in digged]
    min_row, max_row = min(iss), max(iss)
    jss = [j for _, j in digged]
    min_col, max_col = min(jss), max(jss)
    for i in range(min_row, max_row + 1):
        for j in range(min_col, max_col + 1):
            if (i, j) in digged:
                print("# ", end="")
            else:
                print(". ", end="")
        print()
    print()
    
    
def dig_edge(instructions: list[tuple[str, int, str]]) -> list[list[str]]:
    pos = (0, 0)
    digged = {pos}
    for direction, meters, _ in instructions:
        new_pos = pos
        for i in range(1, meters + 1):
            new_pos = (pos[0] + i * DIRECTIONS[direction][0], pos[1] + i * DIRECTIONS[direction][1])
            if new_pos not in digged:
                digged.add(new_pos)
        pos = new_pos
    print_digs(digged)
    
    
def dig_inside():
    
    
if __name__ == "__main__":
    instrs = process_input(read_input(load_dummy=True))
    edge = dig_edge(instrs)

