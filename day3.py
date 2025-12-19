def read_input() -> list[str]:
    with open("input/day3_input.txt") as f:
        return [line.strip() for line in f.readlines()]

def find_max_bank_joltage_part1(bank: str) -> int:
    bank: list[int] = [int(char) for char in bank]
    a = bank[0]
    b = bank[1]

    for i, jolt in enumerate(bank[1:-1], start=1):
        if jolt > a:
            a = jolt
            b = bank[i+1]
        elif jolt > b:
            b = jolt

    if bank[-1] > b:
        b = bank[-1]

    return int(str(a) + str(b))


def find_max_bank_joltage_part2(bank: str) -> int:
    bank: list[int] = [int(char) for char in bank]
    opt_ind = list(range(1, len(bank)))[-12:]

    p = 0 # initialize a pointer

    for i, q in enumerate(opt_ind):
        max_ind = q
        while p < q:
            q -= 1
            if bank[q] >= bank[max_ind]:
                max_ind = q
        p = max_ind + 1
        opt_ind[i] = max_ind

    return int(''.join([str(bank[i]) for i in opt_ind]))


def tot_output_joltage(part="1"):
    seqs = read_input()
    joltages = []
    for bank in seqs:
        if part == "1":
            joltages.append(find_max_bank_joltage_part1(bank))
        if part == "2":
            joltages.append(find_max_bank_joltage_part2(bank))
    return sum(joltages)


if __name__ == '__main__':

    print(tot_output_joltage(part="2"))

