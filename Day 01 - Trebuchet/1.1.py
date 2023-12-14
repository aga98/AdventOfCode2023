import re
from utils import read_input


def word_2_number(s: str) -> int:
    nums = re.findall(r"\d", s)
    combination = nums[0] + nums[-1]
    print(f"{s} --> {combination}")
    return int(combination)


if __name__ == "__main__":
    words = read_input()
    calibration_sum = sum(word_2_number(word) for word in words)
    print(f"CALIBRATION NUMBER: {calibration_sum}")
