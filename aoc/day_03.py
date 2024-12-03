import re


def part_one(file_path: str) -> int:
    """finds any mul(a,b) and calculates the sum of a*b

    Args:
        file_path (str): filepath

    Returns:
        int: sum of products
    """

    # read file
    with open(file_path) as f:
        lines = f.readlines()
    total = 0
    for line in lines:
        for mul_str in re.findall(r"mul\(\d+,\d+\)", line):
            a, b = mul_str[4:-1].split(",")
            total += int(a) * int(b)
    return total


def part_two(file_path: str) -> int:
    """finds any mul(a,b) and calculates the sum of a*b if there is a do()
    and not a don't() before it

    Args:
        file_path (str): filepath

    Returns:
        int: sum of products if turned on
    """

    with open(file_path) as f:
        lines = f.readlines()

    total = 0
    simon_says = True
    for line in lines:
        for mul_str in re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", line):
            if mul_str == "do()":
                simon_says = True
            elif mul_str == "don't()":
                simon_says = False
            else:
                if simon_says:
                    a, b = mul_str[4:-1].split(",")
                    total += int(a) * int(b)
    return total


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_03.txt"))
    print(part_two("aoc/inputs/day_03.txt"))
