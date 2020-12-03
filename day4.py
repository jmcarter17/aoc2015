from utils import timer
from hashlib import md5

KEY = "bgvyzdsv"


def integers_from(n):
    i = n
    while True:
        yield i
        i += 1


def starts_with_nzeros(digest: str, n):
    return digest.startswith("0" * n)


def md5hex(string):
    return md5(string.encode()).hexdigest()


@timer
def solve_part1():
    return next(
        x
        for x in integers_from(100000)
        if starts_with_nzeros(md5hex(f"{KEY}{x}"), 5)
    )


@timer
def solve_part2(part1):
    return next(
        x
        for x in integers_from(1000000)
        if starts_with_nzeros(md5(f"{KEY}{x}".encode()).hexdigest(), 6)
    )


def solve_day4():
    part1 = solve_part1()
    part2 = solve_part2(part1)

    return part1, part2


def main():
    print(solve_day4())


if __name__ == "__main__":
    main()
