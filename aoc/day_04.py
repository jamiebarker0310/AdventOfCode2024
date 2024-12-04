import numpy as np


def part_one(file_path: str) -> int:
    """find all XMAS in any direction
    Args:
        file_path (str): file

    Returns:
        int: number of XMAS's
    """

    # read file
    with open(file_path) as f:
        lines = f.readlines()

    chr_to_int = {char: n for n, char in enumerate("XMAS.")}

    count = 0
    X = np.array([[chr_to_int[char] for char in line.strip()] for line in lines])

    for _ in range(4):
        for i in range(X.shape[0]):
            for j in range(X.shape[1] - 3):
                if (X[i, j : j + 4] == np.array([0, 1, 2, 3])).all():
                    count += 1
        for i in range(X.shape[0] - 3):
            for j in range(X.shape[1] - 3):
                if (np.diag(X[i : i + 4, j : j + 4]) == np.array([0, 1, 2, 3])).all():
                    count += 1

        X = np.rot90(X)

    return count


def part_two(file_path: str) -> int:
    """Calculates any MAS Xs

    Args:
        file_path (str): input filepath

    Returns:
        int: number of MAS Xs
    """

    with open(file_path) as f:
        lines = f.readlines()

    # chr_to_int = {char: n for n, char in enumerate("XMAS.")}

    count = 0
    X = np.array([[char for char in line.strip()] for line in lines])

    for _ in range(4):
        for i in range(X.shape[0] - 2):
            for j in range(X.shape[1] - 2):
                tl = X[i, j] == "M"
                tr = X[i, j + 2] == "S"
                bl = X[i + 2, j] == "M"
                br = X[i + 2, j + 2] == "S"
                c = X[i + 1, j + 1] == "A"

                if all([tl, tr, bl, br, c]):
                    count += 1

        X = np.rot90(X)

    return count


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_04.txt"))
    print(part_two("aoc/inputs/day_04.txt"))
