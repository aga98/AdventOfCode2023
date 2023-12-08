from math import lcm
from utils import read_input
from common import get_instruction, process_input, Node


def get_nodes_ending_with_a(nodes: dict) -> list:
    return [node for node in nodes.values() if node.name.endswith("A")]


def count_steps_to_zs(starting_node: Node, nodes: dict, instructions: str) -> int:
    z_ok = False
    steps = 0
    instructions_gen = get_instruction(instructions)
    while not z_ok:
        instruction = next(instructions_gen)
        node = starting_node
        if instruction == "L":
            starting_node = nodes[node.left]
        elif instruction == "R":
            starting_node = nodes[node.right]
        print(
            f"Node {node.name} [{node.left}|{node.right}] "
            f"-> {starting_node.name} ({instruction})"
        )
        steps += 1
        if starting_node.name.endswith("Z"):
            z_ok = True
    return steps


if __name__ == "__main__":
    instr, node_dict = process_input(read_input(load_dummy=False))
    a_nodes = get_nodes_ending_with_a(node_dict)
    step_nodes = [count_steps_to_zs(a_node, node_dict, instr) for a_node in a_nodes]
    mcm = lcm(*step_nodes)
    print(f"Steps from A's to Z's: {mcm}")
