class Node:
    def __init__(self, name: str, left: str, right: str):
        self.name = name
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.name} -> {self.left} | {self.right}"


def get_instruction(instructions: str):
    i = 0
    while True:
        index = i % len(instructions)
        yield instructions[index]
        i += 1


def process_input(lines: list) -> (str, dict):
    instructions = lines[0]
    nodes = {}
    for line in lines[2:]:
        name = line.split("=")[0].strip()
        lr = line.split("=")[1].strip()
        left = lr.split(",")[0].replace("(", "")
        right = lr.split(",")[1].replace(")", "").strip()
        node = Node(name=name, left=left, right=right)
        nodes[name] = node
    return instructions, nodes
