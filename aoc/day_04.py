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
    X = [[chr_to_int[char] for char in line.strip()] for line in lines]

    for _ in range(4):
        for i in range(len(X)):
            for j in range(len(X[0]) - 3):
                if list(X[i][j : j + 4]) == [0, 1, 2, 3]:
                    count += 1
        for i in range(len(X) - 3):
            for j in range(len(X[0]) - 3):
                if all([X[i + k][j + k] == k for k in range(4)]):
                    count += 1

        X = list(zip(*X[::-1]))

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
    X = [[char for char in line.strip()] for line in lines]

    for _ in range(4):
        for i in range(len(X) - 2):
            for j in range(len(X[0]) - 2):
                tl = X[i][j] == "M"
                tr = X[i][j + 2] == "S"
                bl = X[i + 2][j] == "M"
                br = X[i + 2][j + 2] == "S"
                c = X[i + 1][j + 1] == "A"

                if all([tl, tr, bl, br, c]):
                    count += 1

        X = list(zip(*X[::-1]))

    return count


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_04.txt"))
    print(part_two("aoc/inputs/day_04.txt"))
