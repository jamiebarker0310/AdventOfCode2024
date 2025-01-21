

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
    filesystem = []
    for i, val in enumerate((map(int, lines[0]))):
        if i % 2 == 0:
            filesystem += [i // 2] * val
        else:
            filesystem += [""] * val
    i = 0
    checksum = 0
    while i < len(filesystem):
        if filesystem[i] == "":
            val = filesystem.pop()
            while val == "":
                val = filesystem.pop()
            if i > len(filesystem):
                break
            checksum += val * i
        else:
            checksum += filesystem[i] * i
        i += 1
    return checksum


class FileSystem:
    def __init__(self, start_point, length, value):
        self.start_point = start_point
        self.length = length
        self.value = value

    @property
    def checksum(self):
        return sum(
            [
                self.value * i
                for i in range(self.start_point, self.start_point + self.length)
            ]
        )


def filter_gap(file, gap):

    return file.start_point > gap.start_point and file.length <= gap.length


def part_two(file_path: str):
    """[summary]

    Args:
        file_path (str): [description]

    Returns:
        [type]: [description]
    """

    with open(file_path) as f:
        lines = f.readlines()

    files = []
    gaps = []
    start_point = 0
    for i, v in enumerate(map(int, lines[0])):
        if i % 2 == 0:
            files.append(FileSystem(start_point=start_point, length=v, value=i // 2))
        else:
            gaps.append(FileSystem(start_point=start_point, length=v, value=None))
        start_point += v

    filled_gaps = []

    for file in files[::-1]:
        fitted_gaps = list(filter(lambda x: filter_gap(file, x), gaps))
        if fitted_gaps:
            gap = fitted_gaps[0]
            file.start_point = gap.start_point

            gap.length -= file.length
            gap.start_point += file.length

        filled_gaps.append(file)

    return sum(list(map(lambda x: x.checksum, filled_gaps)))


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_09.txt"))
    print(part_two("aoc/inputs/day_09.txt"))
