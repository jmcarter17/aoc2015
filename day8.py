import time

from utils import timer


def compute_code_count(ln):
    length = len(ln)
    chars = list(ln)
    i = 1
    count = 0
    while i < length - 1:
        count += 1
        if chars[i] == "\\":
            i = i + 4 if chars[i + 1] == "x" else i + 2
        else:
            i += 1
    return count


def compute_repr_count(ln):
    return 2 + ln.count('\\') + ln.count('"') + len(ln)


def process_line(ln):
    length = len(ln)
    count = compute_code_count(ln)
    count2 = compute_repr_count(ln)

    return [ln, length, count, count2]


@timer
def solve_part1(data):
    return sum(x[1] - x[2] for x in data)


@timer
def solve_part2(data):
    return sum(x[3] - x[1] for x in data)


def solve_day8(data):
    part1 = solve_part1(data)
    part2 = solve_part2(data)

    return part1, part2


def main():
    start_time = time.perf_counter()
    with open("inputs/day8.txt") as f:
        data = [process_line(line.strip()) for line in f]
    end_time = time.perf_counter()
    print(f"Finished processing data in {(end_time - start_time)*1000:.4f} ms")

    print(solve_day8(data))


if __name__ == "__main__":
    main()
