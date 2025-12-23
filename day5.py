import bisect


def read_input(denom: int | float = 1E13) -> tuple:
    with open("input/day5_input.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    ranges = lines[0:192]
    ids: list[float] = [int(id_) / denom for id_ in lines[193:]]

    min_max: list[tuple] = []
    for r in ranges:
        min_, max_ = tuple(r.split("-"))
        if denom != 1:
            min_max.append((int(min_) / denom, int(max_) / denom))
        else:
            min_max.append((int(min_), int(max_)))

    # sort min_max list by first element in the tuples
    min_max.sort(key=lambda x: x[0])
    return min_max, ids

def part1():
    ranges, ids = read_input()
    mins = [x[0] for x in ranges]
    fresh_ids = 0
    for id_ in ids:
        min_idx = bisect.bisect_left(mins, id_) - 1
        for cand in ranges[0:min_idx+1]:
            if cand[1] >= id_:
                fresh_ids += 1
                break

    print(f"Found {fresh_ids} fresh ids.")

def part2():
    ranges, _ = read_input(denom=1)

    lmin = -1
    lmax = -1
    dissolved_ranges = []
    for min_, max_ in ranges:
        if min_ > lmax+1:
            if lmin != -1 and lmax != -1:
                dissolved_ranges.append((lmin, lmax))
            lmin = min_
        if max_ >= lmax:
            lmax = max_
    dissolved_ranges.append((lmin, lmax))

    total_fresh = 0
    for min_, max_ in dissolved_ranges:
        total_fresh += (max_ - min_ + 1)
    print(f"Total fresh ids: {total_fresh}")


if __name__ == "__main__":
    part1()
    part2()