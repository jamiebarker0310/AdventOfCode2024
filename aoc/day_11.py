from collections import Counter


def blink(stone: int) -> list[int]:

    if stone == 0:
        return [1]
    len_st = len(str(stone))
    if len_st % 2 == 0:
        return [int(str(stone)[:len_st//2]), int(str(stone)[len_st//2 :])]
    else:
        return [stone*2024]

def run_blinks(file_path, n=25):

    # read file
    with open(file_path) as f:
        lines = f.readlines()

    stones = Counter([int(i) for i in lines[0].split(" ")])

    for i in range(n):
        new_stones = Counter()
        for val, count in stones.items():
            new_counter = Counter(blink(val))
            new_counter = Counter({k: v*count for k,v in new_counter.items()})
            new_stones += new_counter
        stones = new_stones
    return sum(stones.values())


def part_one(file_path: str):
    """[summary]

    Args:
        file_path (str): [description]

    Returns:
        [type]: [description]
    """

    return run_blinks(file_path)


def part_two(file_path: str):
    """[summary]

    Args:
        file_path (str): [description]

    Returns:
        [type]: [description]
    """

    with open(file_path) as f:
        lines = f.readlines()

    return run_blinks(file_path, n=75)


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_11.txt"))
    print(part_two("aoc/inputs/day_11.txt"))
