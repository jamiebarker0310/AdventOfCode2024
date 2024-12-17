def calculate_equations(start: int, remaining: list[int]) -> list[int]:

    options = []

    if len(remaining) == 1:
        return [start + remaining[0], start * remaining[0]]

    options += calculate_equations(start + remaining[0], remaining[1:])
    options += calculate_equations(start * remaining[0], remaining[1:])

    return options


def calculate_equations_two(start: int, remaining: list[int]) -> list[int]:

    options = []

    if len(remaining) == 1:
        return [
            start + remaining[0],
            start * remaining[0],
            int("".join([str(start), str(remaining[0])])),
        ]

    options += calculate_equations_two(start + remaining[0], remaining[1:])
    options += calculate_equations_two(start * remaining[0], remaining[1:])
    options += calculate_equations_two(
        int("".join([str(start), str(remaining[0])])), remaining[1:]
    )

    return options


def part_one(file_path: str):
    """[summary]

    Args:
        file_path (str): [description]

    Returns:
        [type]: [description]
    """

    # read file
    with open(file_path) as f:
        lines = f.readlines()
    total = 0
    for line in lines:
        target, values = line.split(": ")
        target = int(target)
        values = list(map(int, values.split(" ")))
        if target in calculate_equations(values[0], values[1:]):
            total += target

    return total


def part_two(file_path: str):
    """[summary]

    Args:
        file_path (str): [description]

    Returns:
        [type]: [description]
    """

    # read file
    with open(file_path) as f:
        lines = f.readlines()
    total = 0
    for line in lines:
        target, values = line.split(": ")
        target = int(target)
        values = list(map(int, values.split(" ")))
        if target in calculate_equations_two(values[0], values[1:]):
            total += target

    return total


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_07.txt"))
    print(part_two("aoc/inputs/day_07.txt"))
