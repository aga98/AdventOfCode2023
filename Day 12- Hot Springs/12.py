from utils import read_input
from common import process_input


def get_different_arrangements_dp(string: str, groups: list[int]) -> int:
    def get_different_arrangements(string_index: int, group_index: int) -> int:

        if memoization[string_index][group_index] != -1:  # we have already calculated this value
            return memoization[string_index][group_index]

        char = string[string_index - 1]

        if string_index == 0 and group_index == 0:  # we have filled all groups and all characters -> solution found
            # Example: "[#].#.###........." | [1],1,3
            result = 1

        elif string_index == 0:  # we have more groups to fill, but no more characters to fill them with -> no solution
            # Example: "[.].#.###........." 1, | 1,[1],3
            result = 0

        elif group_index == 0:  # we are on the last group, if all the characters from
            # the beginning to the current index are "." (or "?"), we have a solution, otherwise we don't.
            # Example: "..?..????....[#].#.###........." | [1],1,3
            previous_chars = set(string[:string_index])
            result = 0 if '#' in previous_chars else 1

        elif char == '.':  # simple case: ending "." don't affect the result -> remove the "."
            # Example: "#.#.###.........[.]" | 1,1,[3]
            result = get_different_arrangements(string_index - 1, group_index)  # [#.#.###.........] 1,1,3

        else:  # char is "#" or "?" and we have more groups to fill
            contiguous_damaged = groups[group_index - 1]
            # check if current group of "#" is contiguous
            # - we cannot have a contiguous group if the current index is smaller than the group size:
            #   Example: "#[###]..." -> "3"
            # - we cannot have a contiguous group if there is a "." in the group:
            #   Example: ".[.##].." -> "3"
            # - we cannot have a contiguous group if the previous character is "#" as the contiguous group would be bigger:
            #   Example: "..#[###]..." -> "3"
            dot_in_group = "." in string[string_index - contiguous_damaged:string_index]
            if contiguous_damaged > string_index or dot_in_group:
                result = 0
            elif string_index > contiguous_damaged and string[string_index - contiguous_damaged - 1] == '#':
                result = 0
            else:
                # if we have a valid group, move to the previous group and try to fill it
                # Example: From "#.#.##[#]" | 1,1,[3], move to "#.#[.]###" | 1,[1],3
                result = get_different_arrangements(max(string_index - contiguous_damaged - 1, 0), group_index - 1)

            if char == '?':
                # if we have a "?", we can also try to fill the previous group (if it works with we will add one more)
                result += get_different_arrangements(string_index - 1, group_index)

        memoization[string_index][group_index] = result
        return result

    memoization = [[-1 for _ in range(len(groups) + 1)] for _ in range(len(string) + 1)]
    arrangements = get_different_arrangements(len(string), len(groups))
    print(f"Arrangements for {string} and {groups}: {arrangements}")
    return arrangements


if __name__ == "__main__":
    field = process_input(read_input())
    different_arrangements_sum_1 = sum(get_different_arrangements_dp(s, gr) for s, gr in field)
    different_arrangements_sum_2 = sum(get_different_arrangements_dp("?".join([s]*5), gr*5) for s, gr in field)
    print(f"==> Sum of different arrangements (part 1): {different_arrangements_sum_1}")
    print(f"==> Sum of different arrangements (part 2): {different_arrangements_sum_2}")
