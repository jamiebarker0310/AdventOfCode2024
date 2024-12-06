from collections import defaultdict


def part_one(file_path: str) -> int:
    """get the median sum of the number of ordered updates

    Args:
        file_path (str): filepath

    Returns:
        int: median sum of ordered updates
    """

    # read file
    with open(file_path) as f:
        lines = f.readlines()

    rules = defaultdict(set)
    i = 0
    while lines[i] != "\n":
        a, b = lines[i].split("|")
        rules[int(a)].add(int(b))
        i += 1
    total = 0
    for line in lines[i + 1 :]:
        update = list(map(int, line.split(",")))
        if all([rules[update[j]] >= set(update[j + 1 :]) for j in range(len(update))]):

            total += update[(len(update) // 2)]

    return total


def part_two(file_path: str) -> int:
    """get the median sum of the number of corrected unordered updates

    Args:
        file_path (str): filepath

    Returns:
        int: median sum of the number of corrected unordered updates
    """

    with open(file_path) as f:
        lines = f.readlines()
    rules = defaultdict(set)
    i = 0
    while lines[i] != "\n":
        a, b = lines[i].split("|")
        rules[int(a)].add(int(b))
        i += 1
    total = 0
    for line in lines[i + 1 :]:
        update = list(map(int, line.split(",")))
        if not all(
            [rules[update[j]] >= set(update[j + 1 :]) for j in range(len(update))]
        ):
            total += sorted(update, key=lambda x: len(rules[x] & set(update)))[
                len(update) // 2
            ]
    return total


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_05.txt"))
    print(part_two("aoc/inputs/day_05.txt"))
