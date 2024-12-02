def calculate_safety(line: list[int]) -> bool:
    diffs = [line[i] - line[i + 1] for i in range(len(line) - 1)]

    monotonous = all(map(lambda x: x > 0, diffs)) or all(map(lambda x: x < 0, diffs))
    small = all(map(lambda x: abs(x) <= 3, diffs))

    return monotonous and small


def calculate_adjusted_safety(line: list[int]) -> bool:

    for i in range(len(line)):
        removed_line = line[:i] + line[i + 1 :]
        if calculate_safety(removed_line):
            return True
    return False


def part_one(file_path: str):
    """calculate how many lines are safe

    Args:
        file_path (str): [description]

    Returns:
        int: number of safe lines
    """

    # read file
    with open(file_path) as f:
        lines = f.readlines()
    count = 0
    for line in lines:
        line = list(map(int, line.split(" ")))
        if calculate_safety(line):
            count += 1

    return count


def part_two(file_path: str) -> int:
    """how many of lines are safe-ish?

    Args:
        file_path (str): [description]

    Returns:
        int: number of safeish lines
    """

    with open(file_path) as f:
        lines = f.readlines()
    count = 0
    for line in lines:
        line = list(map(int, line.split(" ")))
        if calculate_safety(line):
            count += 1

        elif calculate_adjusted_safety(line):
            count += 1

    return count


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_02.txt"))
    print(part_two("aoc/inputs/day_02.txt"))
