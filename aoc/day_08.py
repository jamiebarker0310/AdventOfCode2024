def in_grid(n, x, y):

    return n.real <= x and n.imag <= y and min(n.real, n.imag) >= 0


def get_antinodes(a_list: list[complex], x, y):

    antinodes = set()
    for a1 in a_list:
        for a2 in a_list:
            n = (a2 - a1) + a2
            if a2 != a1 and in_grid(n, x, y):
                antinodes.add((a2 - a1) + a2)
    return antinodes


def get_harmonic_antinodes(a_list: list[complex], x, y):

    antinodes = set()
    for a1 in a_list:
        for a2 in a_list:
            i = 0
            while in_grid(i * (a2 - a1) + a2, x, y) and a2 != a1:
                antinodes.add(i * (a2 - a1) + a2)
                i += 1
    return antinodes


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

    antennae = {}
    for y, line in enumerate(lines[::-1]):
        for x, char in enumerate(line.strip()):
            if char != ".":
                antennae[char] = antennae.get(char, []) + [x + y * 1j]

    antinodes = set()
    for a_list in antennae.values():
        antinodes |= get_antinodes(a_list, x, y)

    return len(antinodes)


def part_two(file_path: str):
    """[summary]

    Args:
        file_path (str): [description]

    Returns:
        [type]: [description]
    """

    with open(file_path) as f:
        lines = f.readlines()

    antennae = {}
    for y, line in enumerate(lines[::-1]):
        for x, char in enumerate(line.strip()):
            if char != ".":
                antennae[char] = antennae.get(char, []) + [x + y * 1j]

    antinodes = set()
    for a_list in antennae.values():
        antinodes |= get_harmonic_antinodes(a_list, x, y)

    return len(antinodes)


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_08.txt"))
    print(part_two("aoc/inputs/day_08.txt"))
