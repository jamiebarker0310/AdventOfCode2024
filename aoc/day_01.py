from collections import Counter


def part_one(file_path: str) -> int:
    """sorts both columns and calculates absolute difference

    Args:
        file_path (str): path to input

    Returns:
        int: similarity score
    """

    # read file
    with open(file_path) as f:
        lines = f.readlines()
    
    col1 = sorted([int(l.split("   ")[0]) for l in lines])
    col2 = sorted([int(l.split("   ")[1]) for l in lines])

    return sum(map(lambda x: abs(x[0]-x[1]), zip(col1, col2)))


def part_two(file_path: str) -> int:
    """calculates count of col1 in col2 and returns the sum of
    col1 * count of col2

    Args:
        file_path (str): path to input

    Returns:
        int: similarity score
    """

    with open(file_path) as f:
        lines = f.readlines()
    
    col1 = [int(l.split("   ")[0]) for l in lines]
    col2_counter = Counter([int(l.split("   ")[1]) for l in lines])

    return sum([x*col2_counter[x] for x in col1])



if __name__ == "__main__":
    print(part_one("aoc/inputs/day_01.txt"))
    print(part_two("aoc/inputs/day_01.txt"))
