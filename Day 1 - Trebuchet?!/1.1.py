import re


def word_2_number(s: str) -> int:
    nums = re.findall(r"\d", s)
    combination = nums[0] + nums[-1]
    print(f"{s} --> {combination}")
    return int(combination)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        words = f.readlines()
    calibration_sum = sum(word_2_number(word.replace("\n", "")) for word in words)
    print(f"CALIBRATION NUMBER: {calibration_sum}")
