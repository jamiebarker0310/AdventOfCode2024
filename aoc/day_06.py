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
    
    barriers = []
    for x, line in enumerate(lines[::-1]):
        for y, char in enumerate(line.strip()):
            if char == "#":
                barriers.append(y + x*1j)
            elif char != ".":
                pos = y + x*1j

    increment = 0 + 1j
    locations = set()
    while min(pos.real, pos.imag) >= 0 and pos.real < x and pos.imag < y:
        
        if pos + increment in barriers:
            increment *= -1j
        locations.add(pos)
        pos += increment

    return len(locations)


def part_two(file_path: str):
    """[summary]

    Args:
        file_path (str): [description]

    Returns:
        [type]: [description]
    """

    return None
    # with open(file_path) as f:
    #     lines = f.readlines()
    # # parse barriers and position
    # barriers = set()
    # for x, line in enumerate(lines[::-1]):
    #     for y, char in enumerate(line.strip()):
    #         if char == "#":
    #             barriers.add(y + x*1j)
    #         elif char != ".":
    #             pos = y + x*1j

    # ## Get all points on the path
    # increment = 0 + 1j
    # positions = set()
    # while min(pos.real, pos.imag) >= 0 and pos.real < x and pos.imag < y:
        
    #     if pos + increment in barriers:
    #         increment *= -1j
    #     positions.add(pos)
    #     pos += increment

    # # get all positions adjacent to barriers that map to barriers and the position 
    # # where they would change direction
    # pos_to_bar = {}
    # for barrier in barriers:
    #     for pos_rel in [1j, -1j, 1, -1]:
    #         pos = barrier + pos_rel
    #         inc = pos_rel * 1j
    #         while min(pos.real, pos.imag) >= 0 and pos.real < x and pos.imag < y:
    #             if pos + inc in barriers:
    #                 pos_to_bar[barrier + pos_rel] = pos
    #                 break
    #             pos += inc

    # for pos in positions:

    
    
    # inc = 0 + 1j
    # positions = set()
    # loop_barriers = set()
    # while min(pos.real, pos.imag) >= 0 and pos.real < x and pos.imag < y:
    #     if pos + inc in barriers:
    #         inc *= -1j
    #     positions.add((pos, inc))
    #     pos += inc

    #     ### Adding simulation of adding barrier in front
    #     new_barriers = barriers | set([pos + inc])
    #     new_pos, new_inc = pos + inc*-1j, inc*-1j
    #     new_positions = positions | set([(new_pos, new_inc)])
    #     if check_for_loop(new_pos, new_inc, new_positions, new_barriers, x, y):
    #         loop_barriers.add(pos + inc)
        
    # return len(pos_to_bar)

# def check_for_loop(pos, inc, positions, barriers, x, y):

#     while min(pos.real, pos.imag) >= 0 and pos.real < x and pos.imag < y:
#         if pos + inc in barriers:
#             inc *= -1j
#         if (pos +inc, inc) in positions:
#             return True
#         positions.add((pos, inc))
#         pos += inc

#     return False

if __name__ == "__main__":
    print(part_one("aoc/inputs/day_06.txt"))
    print(part_two("aoc/inputs/day_06.txt"))
