from math import prod

from utils import timer


def process_line(ln):
    dims = [int(x) for x in ln.split('x')]
    return sorted(dims)


def area(dims):
    l, w, h = dims
    return 2 * (l*w + l*h + w*h) + l*w


def smallest_perimeter(dims):
    l, w, _ = dims
    return 2 * (l+w)


def cube(dims):
    return prod(dims)


def solve_day2(dims):
    part1 = solve_part1(dims)
    part2 = solve_part2(dims)
    return part1, part2


@timer
def solve_part1(dims):
    return sum(area(dim) for dim in dims)


@timer
def solve_part2(data):
    return sum(smallest_perimeter(ln) + cube(ln) for ln in data)


def main():
    with open("inputs/day2.txt") as f:
        dimensions = [process_line(line.strip()) for line in f]

    print(solve_day2(dimensions))


if __name__ == "__main__":
    main()
