import re
from utils import read_input


NUMBER = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


def word_2_number_v2(s: str) -> int:
    string_nums = "|".join(list(NUMBER.keys()))
    nums = re.findall(rf"(?=(\d|{string_nums}))", s)
    nums_int = [NUMBER.get(n, n) for n in nums]
    combination = nums_int[0] + nums_int[-1]
    print(f"{s} --> {combination}")
    return int(combination)


if __name__ == "__main__":
    words = read_input()
    calibration_sum = sum(word_2_number_v2(word) for word in words)
    print(f"CALIBRATION NUMBER: {calibration_sum}")
