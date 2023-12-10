from utils import read_input
from common import process_input


def extrapolate_next_value(history: list) -> int:
    if len(set(history)) == 1:
        return history[0]
    diffs = [history[i + 1] - history[i] for i in range(len(history) - 1)]
    return history[-1] + extrapolate_next_value(diffs)


if __name__ == "__main__":
    histories = process_input(read_input())
    sums = 0
    for hist in histories:
        extrapolation = extrapolate_next_value(hist)
        sums += extrapolation
        print(f"{hist} -> {extrapolation}")
    print(f"Total: {sums}")

