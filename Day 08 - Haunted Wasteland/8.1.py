from utils import read_input
from common import get_instruction, process_input


def count_steps_to_zzz(nodes: dict, instructions: str) -> int:
    zzz_found = False
    node = nodes["AAA"]
    steps = 0
    instructions_gen = get_instruction(instructions)
    while not zzz_found:
        instruction = next(instructions_gen)
        current_node = node
        if instruction == "L":
            node = nodes[node.left]
        elif instruction == "R":
            node = nodes[node.right]
        print(
            f"Node {current_node.name} [{current_node.left}|{current_node.right}] "
            f"-> {node.name} ({instruction})"
        )
        steps += 1
        if node.name == "ZZZ":
            zzz_found = True
    return steps


if __name__ == "__main__":
    instr, node_dict = process_input(read_input())
    num_steps = count_steps_to_zzz(node_dict, instr)
    print(f"Steps from AAA to ZZZ: {num_steps}")
