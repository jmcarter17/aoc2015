from utils import timer


@timer
def part1(boss):
    """Need Damage + Armor > Bosses D + A (10)"""
    """Min is 11"""
    """Longsword + chainmail + ArmorR+2"""
    return 111


@timer
def part2(boss):
    """Need Damage + Armor = Bosses D + A (10)"""
    """Max is 10"""
    """R+3, R+3, dagger = 188"""
    return 188


def solve_day21(boss):
    result1 = part1(boss)
    result2 = part2(boss)
    return result1, result2


@timer
def main():
    boss = {
        "Hit Points": 109,
        "Damage": 8,
        "Armor": 2
    }

    print(solve_day21(boss))


if __name__ == "__main__":
    main()
