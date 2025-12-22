import copy


def read_input() -> list[list]:
    with open("input/day4_input.txt") as f:
        return [list(line.strip()) for line in f.readlines()]


def part1() -> int:
    grid = read_input()
    total_accessible = 0
    for row_idx, row in enumerate(grid):
        for roll_idx, item in enumerate(row):
            if item != "@":
                continue
            if accessible(grid, row_idx, roll_idx):
                total_accessible += 1

    return total_accessible

def part2() -> int:
    grid = read_input()
    total_accessed = 0
    while True:
        grid_copy = copy.deepcopy(grid)
        accessed_at_start = total_accessed
        for row_idx, row in enumerate(grid):
            for roll_idx, item in enumerate(row):
                if item != "@":
                    continue
                if accessible(grid, row_idx, roll_idx):
                    total_accessed += 1
                    grid_copy[row_idx][roll_idx] = "."
        if total_accessed == accessed_at_start:
            break
        grid = grid_copy

    return total_accessed

def accessible(grid: list[list], row_idx: int, roll_idx: int) -> bool:
    neighbors = [
        (row_idx - 1, roll_idx-1),
        (row_idx - 1, roll_idx),
        (row_idx - 1, roll_idx + 1),
        (row_idx, roll_idx -1),
        (row_idx, roll_idx + 1),
        (row_idx+1, roll_idx-1),
        (row_idx+1, roll_idx),
        (row_idx+1, roll_idx+1),
    ]

    neighbor_roll_count = 0
    for neighbor_idx in neighbors:
        try:
            if neighbor_idx[0] >=0 and neighbor_idx[1] >= 0:
                neighbor_item = grid[neighbor_idx[0]][neighbor_idx[1]]
                if neighbor_item == "@":
                    neighbor_roll_count += 1
        except IndexError:
            pass

    if neighbor_roll_count < 4:
        return True
    else:
        return False



if __name__ == "__main__":
    total = part2()
    print(total)