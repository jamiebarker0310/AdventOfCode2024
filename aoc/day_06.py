def walk(G, start):

    pos, v, seen = start, 1j, set()

    while pos in G and (pos, v) not in seen:
        seen.add((pos, v))
        if G.get(pos + v) == "#":
            v *= -1j
        else:
            pos += v
    return {s[0] for s in seen}, (pos, v) in seen


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

    G = {}
    for y, line in enumerate(lines[::-1]):
        for x, char in enumerate(line.strip()):
            G[x + y * 1j] = char
            if char == "^":
                start = x + y * 1j

    return len(walk(G, start)[0])


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
    G = {}
    for y, line in enumerate(lines[::-1]):
        for x, char in enumerate(line.strip()):
            G[x + y * 1j] = char
            if char == "^":
                start = x + y * 1j

    path = walk(G, start)[0]

    return sum(walk(G | {barrier: "#"}, start)[1] for barrier in path)


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_06.txt"))
    print(part_two("aoc/inputs/day_06.txt"))
