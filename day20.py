from utils import timer, integers_from


def factors(n):
    return set(
        factor for i in range(1, int(n**0.5) + 1) if n % i == 0
        for factor in (i, n//i)
    )


def count_presents(house):
    return sum(factor * 10 for factor in factors(house))


def count_presents2(house):
    return sum(factor * 11 for factor in factors(house) if house // factor <= 50)


@timer
def part1(number):
    presents = (count_presents(house) for house in integers_from(500000))
    filtered_presents = (i for i, pres in enumerate(presents) if pres >= number)

    return next(filtered_presents) + 500000


@timer
def part2(number, result1):
    presents = (count_presents2(house) for house in integers_from(result1))
    filtered_presents = (i for i, pres in enumerate(presents) if pres >= number)

    return next(filtered_presents) + result1


def solve_day20(number):
    result1 = part1(number)
    result2 = part2(number, result1)
    return result1, result2


@timer
def main():
    print(solve_day20(29000000))


if __name__ == "__main__":
    main()
