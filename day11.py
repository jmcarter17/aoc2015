from utils import timer


def c2i(c):
    return ord(c) - ord('a')


def i2c(i):
    return chr(i + ord('a'))


def add1(c):
    nexti = c2i(c) + 1
    if nexti == c2i('i') or nexti == c2i('o') or nexti == c2i('l'):
        nexti += 1
    of = nexti == 26
    if of:
        nexti %= 26

    nextc = i2c(nexti)

    return nextc, of


def next_pwd(pwd):
    new = list(reversed(pwd))
    for i, c in enumerate(new):
        new[i], of = add1(c)
        if not of:
            break

    return "".join(list(reversed(new)))


def pwd_valid(pwd):
    if any(c in 'iol' for c in pwd):
        return False

    if not any(c2i(c2) - c2i(c1) == 1 and c2i(c3) - c2i(c2) == 1 for c1, c2, c3 in zip(pwd, pwd[1:], pwd[2:])):
        return False

    if len(set([c for c in zip(pwd, pwd[1:]) if c[0] == c[1]])) < 2:
        return False

    return True


@timer
def solve_part1(initial):
    pwd = next_pwd(initial)
    while not pwd_valid(pwd):
        pwd = next_pwd(pwd)

    return pwd


@timer
def solve_part2(initial):
    return solve_part1(initial)


def solve_day11(initial):
    part1 = solve_part1(initial)
    part2 = solve_part2(part1)

    return part1, part2


def main():
    initial = "vzbxkghb"

    print(solve_day11(initial))


if __name__ == "__main__":
    main()
