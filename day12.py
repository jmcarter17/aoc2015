from utils import timer
import json


def solve_part1(data):
    if isinstance(data, int):
        return data
    elif isinstance(data, list):
        return sum(solve_part1(item) for item in data)
    elif isinstance(data, dict):
        return sum(solve_part1(item) for item in data.values())
    else:
        return 0


def solve_part2(data):
    if isinstance(data, int):
        return data
    elif isinstance(data, list):
        return sum(solve_part2(item) for item in data)
    elif isinstance(data, dict):
        if "red" in data.values():
            return 0
        else:
            return sum(solve_part2(item) for item in data.values())
    else:
        return 0


@timer
def solve_day12(data):
    part1 = solve_part1(data)
    part2 = solve_part2(data)

    return part1, part2


def main():
    with open('inputs/day12.json') as f:
        data = json.load(f)

    print(solve_day12(data))


if __name__ == "__main__":
    main()
