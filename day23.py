from utils import timer


def process_line(ln):
    items = ln.split()
    items[1] = items[1].replace(",", "")

    return items


def do_op(data, a, b, idx):
    op = data[idx]
    action = op[0]
    if action == 'inc':
        if op[1] == 'a':
            a += 1
        else:
            b += 1
    elif action == 'hlf':
        a //= 2
    elif action == 'tpl':
        a *= 3
    elif action == 'jmp':
        idx += int(op[1]) - 1
    elif action == 'jie':
        if a % 2 == 0:
            idx += int(op[2]) - 1
    elif action == 'jio':
        if a == 1:
            idx += int(op[2]) - 1

    idx += 1
    return a, b, idx


@timer
def part1(data):
    a, b = 0, 0
    idx = 0
    while idx < len(data):
        a, b, idx = do_op(data, a, b, idx)

    return b


@timer
def part2(data):
    a, b = 1, 0
    idx = 0
    while idx < len(data):
        a, b, idx = do_op(data, a, b, idx)

    return b


def solve_day23(data):
    result1 = part1(data)
    result2 = part2(data)
    return result1, result2


@timer
def main():
    with open("inputs/day23.txt") as f:
        data = [process_line(ln.strip()) for ln in f]

    print(solve_day23(data))


if __name__ == "__main__":
    main()
