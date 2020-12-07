from utils import timer


skeleton_key = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


def process_line(ln):
    idx = ln.find(":")
    key = ln[:idx]
    itms = dict([item.strip().split(': ') for item in ln[idx + 1:].split(", ")])
    return key, {k: int(itms[k]) for k in itms}


def check_ok(vals):
    for k in vals:
        if check_key(k, vals[k]) is False:
            return False
    return True


def check_key(k, val):
    if k == 'trees' or k == 'cats':
        if val <= skeleton_key[k]:
            return False
    elif k == 'pomeranians' or k == 'goldfish':
        if val >= skeleton_key[k]:
            return False
    elif val != skeleton_key[k]:
        return False
    return True


def solve_day16(data):
    ans = 0
    for sue, val in data.items():
        if all(item in skeleton_key.items() for item in val.items()):
            ans = sue
            break

    ans2 = 0
    for sue, vals in data.items():
        if check_ok(vals):
            ans2 = sue
            break

    return ans, ans2


@timer
def main():
    with open("inputs/day16.txt") as f:
        data = dict([process_line(ln) for ln in f])

    print(solve_day16(data))


if __name__ == "__main__":
    main()
