import re


def symbol_in_surroundings(matrix, row: int, col_start: int, col_end: int) -> bool:
    symbols = r"/[-@!$%^&*()_+#|~=`{}\[\]:"
    upper_bottom_cols = range(max(0, col_start - 1), min(col_end + 2, len(matrix[row])))

    if (  # check if symbol is in the same row (left or right)
        (col_start != 0 and matrix[row][col_start-1] in symbols)
        or (col_end != len(matrix[row]) and matrix[row][col_end+1] in symbols)
    ):
        return True

    # check if symbol is in the upper or bottom row
    for j in upper_bottom_cols:
        if row != 0 and matrix[row-1][j] in symbols:
            return True
        if row != len(matrix) - 1 and matrix[row+1][j] in symbols:
            return True
    return False


def process_row(matrix, i: int) -> int:
    row = matrix[i][:-1] if matrix[i][-1] == "\n" else matrix[i]
    findings = re.finditer(r"\d+", "".join(row))
    row_sum = 0
    for match in findings:
        col_start = match.start()
        col_end = match.end() - 1
        number = match.group()
        sum_value = int(number) if symbol_in_surroundings(matrix, i, col_start, col_end) else 0
        print(f"row: {i}, col_start: {col_start}, col_end: {col_end}, number: {number}, sum_value: {sum_value}")
        row_sum += sum_value
    return row_sum


def process_matrix(matrix):
    result = sum(process_row(matrix, i) for i, row in enumerate(matrix))
    print(result)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        mat = f.readlines()
    process_matrix(mat)

