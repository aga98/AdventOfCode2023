def process_input(lines: list[str]) -> list[list[str]]:
    valley_list = [[]]
    num_valley = 0
    for line in lines:
        if line != "":
            valley_list[num_valley].append(line)
        else:
            valley_list.append([])
            num_valley += 1
    return valley_list


def check_reflections(reflection_line: int, valley: list[str]) -> int:
    """
    Validate it is actually a reflection line
    """
    l = reflection_line
    r = reflection_line + 1
    matches = 0
    while l >= 0 and r < len(valley):
        if valley[l] != valley[r]:
            return False
        matches += 1
        l -= 1
        r += 1
    return True
