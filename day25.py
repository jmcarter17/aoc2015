from utils import timer


def next_index(idx):
    new = (idx[0] - 1, idx[1] + 1)
    if new[0] < 1:
        new = (new[1], 1)

    return new


def next_code(code):
    return (code * 252533) % 33554393


@timer
def main():
    wanted_idx = (2947, 3029)
    code = 20151125

    idx = (1, 1)
    while idx != wanted_idx:
        idx = next_index(idx)
        code = next_code(code)

    print(idx, code)


if __name__ == "__main__":
    main()
