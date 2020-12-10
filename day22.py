from utils import timer


@timer
def part1(boss):
    return None


@timer
def part2(boss):
    return None


def solve_day22(boss):
    result1 = part1(boss)
    result2 = part2(boss)
    return result1, result2


@timer
def main():
    boss = {
        "HP": 58,
        "Damage": 9
    }

    print(solve_day22(boss))


if __name__ == "__main__":
    main()
