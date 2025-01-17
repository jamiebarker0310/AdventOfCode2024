from aoc.day_10 import part_one, part_two

def test_part_one():

    test_file_path = "tests/test_inputs/test_day_10.txt"

    assert part_one(test_file_path) == 36

def test_part_one_simple():

    test_file_path = "tests/test_inputs/test_day_10_simple.txt"

    assert part_one(test_file_path) == 4

def test_part_two():

    test_file_path = "tests/test_inputs/test_day_10.txt"

    assert part_two(test_file_path) == 81