from utils import read_input

DIRECTIONS = {
    "N": (-1, 0),
    "S": (1, 0),
    "E": (0, 1),
    "W": (0, -1),
}


def process_input(lines: list[str]) -> list[list[str]]:
    return [list(line) for line in lines]


class Cavern:
    def __init__(self, cavern: list[list[str]]):
        self.cavern = cavern
        self.beams = [Beam(0, 0, "E")]
        self.visited_tiles = set()
    
    def move_beams(self):
        while len(self.beams) > 0:
            for beam in self.beams:
                new_beams = beam.move(self.cavern)
                if not beam.ended:
                    self.visited_tiles.add((beam.i, beam.j))
                if new_beams is not None:
                    new_beam_1, new_beam_2 = new_beams
                    self.beams += [new_beam_1, new_beam_2]
                else:
                    self.beams.remove(beam)


class Beam:
    def __init__(self, i: int, j: int, direction: str):
        self.i = i
        self.j = j
        self.direction = direction
        self.ended = False
    
    def move(self, cavern: list[list[str]]) -> tuple["Beam", "Beam"] | None:
        next_i = self.i + DIRECTIONS[self.direction][0]
        next_j = self.j + DIRECTIONS[self.direction][1]
        if next_i < 0 or next_i == len(cavern) or next_j < 0 or next_j == len(cavern[0]):
            self.ended = True
        else:
            tile = cavern[next_i][next_j]
            if tile not in ["|", "-"]:
                if tile == "/" and self.direction == "E":
                    self.direction = "N"
                elif tile == "\\" and self.direction == "E":
                    self.direction = "S"
                elif tile == "/" and self.direction == "W":
                    self.direction = "S"
                elif tile == "\\" and self.direction == "W":
                    self.direction = "N"
                elif tile == "/" and self.direction == "N":
                    self.direction = "E"
                elif tile == "\\" and self.direction == "N":
                    self.direction = "W"
                elif tile == "/" and self.direction == "S":
                    self.direction = "W"
                elif tile == "\\" and self.direction == "S":
                    self.direction = "E"
                self.i = next_i
                self.j = next_j
            else:
                if tile == "|" and self.direction in ["W", "E"]:
                    new_beam_1 = Beam(next_i, next_j, "N")
                    new_beam_2 = Beam(next_i, next_j, "S")
                    return new_beam_1, new_beam_2
                elif tile == "-" and self.direction in ["N", "S"]:
                    new_beam_1 = Beam(next_i, next_j, "E")
                    new_beam_2 = Beam(next_i, next_j, "W")
                    return new_beam_1, new_beam_2
                else:
                    self.i = next_i
                    self.j = next_j
                

def find_tiles_energized():
    c = process_input(read_input(load_dummy=True))
    cavern = Cavern(c)
    cavern.move_beams()
    print(f"Part 1 - tiles visited: {len(cavern.visited_tiles)}")
    

if __name__ == "__main__":
    find_tiles_energized()
