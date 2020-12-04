from utils import timer


def get_index(i, j):
    return i + 1000 * j


def actions(lights, ln):
    action, bl, tr = ln
    for i in range(bl[0], tr[0] + 1):
        for j in range(bl[1], tr[1] + 1):
            apply_action(lights, action, get_index(i, j))


def actions_2(lights, ln):
    action, bl, tr = ln
    for i in range(bl[0], tr[0] + 1):
        for j in range(bl[1], tr[1] + 1):
            apply_action_2(lights, action, get_index(i, j))


def apply_action(lights, action, index):
    if action == "on":
        lights[index] = 1
    elif action == "off":
        lights[index] = 0
    else:
        lights[index] = not lights[index]


def apply_action_2(lights, action, index):
    if action == "on":
        lights[index] += 1
    elif action == "off" and lights[index] > 0:
        lights[index] -= 1
    elif action == "toggle":
        lights[index] += 2


def process_line(ln):
    items = ln.split()
    if items[0] == "turn":
        items.pop(0)
    action = items[0]
    bl = [int(x) for x in items[1].split(",")]
    tr = [int(x) for x in items[3].split(",")]
    return action, bl, tr


@timer
def solve_part1(data):
    lights = [0] * 1000000
    for ln in data:
        actions(lights, ln)
    return sum(lights)


@timer
def solve_part2(data):
    lights = [0] * 1000000
    for ln in data:
        actions_2(lights, ln)
    return sum(lights)


def solve_day6(data):
    part1 = solve_part1(data)
    part2 = solve_part2(data)

    return part1, part2


def main():
    with open("inputs/day6.txt") as f:
        data = [process_line(line.strip()) for line in f]
    print(solve_day6(data))


if __name__ == "__main__":
    main()
