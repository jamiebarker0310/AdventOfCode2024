from collections import defaultdict


def get_all_paths(file_path):

    # read file
    with open(file_path) as f:
        lines = f.readlines()
    pos_to_height = {}
    for i, line in enumerate(lines[::-1]):
        for j, char in enumerate(line.strip()):
            pos_to_height[j + i * 1j] = int(char) if char.isdigit() else 100

    nodes = defaultdict(list)
    for pos1, h1 in pos_to_height.items():
        for diff in [1, -1, 1j, -1j]:
            if pos_to_height.get(pos1 + diff) == h1 + 1:
                nodes[pos1].append(pos1 + diff)

    paths = [[k] for k, v in pos_to_height.items() if v == 0]
    for i in range(10 - 1):
        new_paths = []
        for path in paths:
            for next_step in nodes.get(path[-1], []):
                new_paths.append(path + [next_step])
        paths = new_paths

    return paths


def part_one(file_path: str, n=10):
    """[summary]

    Args:
        file_path (str): [description]

    Returns:
        [type]: [description]
    """

    paths = get_all_paths(file_path)
    return len({(p[0], p[-1]) for p in paths})


def part_two(file_path: str):
    """[summary]

    Args:
        file_path (str): [description]

    Returns:
        [type]: [description]
    """

    paths = get_all_paths(file_path)
    return len(paths)


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_10.txt"))
    print(part_two("aoc/inputs/day_10.txt"))
