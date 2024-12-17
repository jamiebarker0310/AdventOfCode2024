from aoc.day_08 import part_one, part_two


def test_part_one():

    test_file_path = "tests/test_inputs/test_day_08.txt"

    assert part_one(test_file_path) == 14


def test_part_two():

    test_file_path = "tests/test_inputs/test_day_08.txt"

    assert part_two(test_file_path) == 34
