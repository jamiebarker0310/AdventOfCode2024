import re
from math import isclose


def is_int(x):

    return isclose(x, round(x), rel_tol=0, abs_tol=1e-3)


def valid_solution(na, nb):

    return is_int(na) and is_int(nb) and min(na, nb) >= 0


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
    data = []

    buttons = []
    for i, line in enumerate(lines):
        if i % 4 == 3:
            data.append(buttons)
            buttons = []
        else:
            x, y = tuple(map(lambda x: int(re.findall(r"\d+", x)[0]), line.split(", ")))
            buttons += [x, y]
    data.append(buttons)

    tokens = 0
    for buttons in data:
        xa, ya, xb, yb, xp, yp = buttons
        det = 1 / (xa * yb - xb * ya)
        na = (yb * xp - xb * yp) * det
        nb = (xa * yp - ya * xp) * det

        if valid_solution(na, nb):
            tokens += 3 * na
            tokens += nb

    return int(tokens)


def part_two(file_path: str):
    """[summary]

    Args:
        file_path (str): [description]

    Returns:
        [type]: [description]
    """

    with open(file_path) as f:
        lines = f.readlines()
    data = []

    buttons = []
    for i, line in enumerate(lines):
        if i % 4 == 3:
            data.append(buttons)
            buttons = []
        else:
            x, y = tuple(map(lambda x: int(re.findall(r"\d+", x)[0]), line.split(", ")))
            buttons += [x, y]
    data.append(buttons)

    tokens = 0
    for buttons in data:
        xa, ya, xb, yb, xp, yp = buttons

        xp += 10000000000000
        yp += 10000000000000

        det = 1 / (xa * yb - xb * ya)
        na = (yb * xp - xb * yp) * det
        nb = (xa * yp - ya * xp) * det

        if valid_solution(na, nb):
            tokens += 3 * na
            tokens += nb

    return int(tokens)


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_13.txt"))
    print(part_two("aoc/inputs/day_13.txt"))
