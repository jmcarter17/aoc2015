from utils import timer


def process_line(ln):
    items = ln.split()
    name = items[0]
    speed = int(items[3])
    time = int(items[6])
    rest = int(items[13])
    return name, speed, time, rest


def distance(total_time, deer):
    name, speed, time, rest = deer
    cycle_time = time + rest
    cycle_distance = speed * time
    num_cycles = total_time // cycle_time
    extra_time = min(total_time % cycle_time, time)
    total_distance = cycle_distance * num_cycles + extra_time * speed

    return total_distance, name


def solve_day14(data):
    _TOTAL_TIME = 2503
    dist1 = (distance(_TOTAL_TIME, deer) for deer in data)

    points = {deer[0]: 0 for deer in data}
    for sec in range(1, _TOTAL_TIME + 1):
        distances = (distance(sec, deer) for deer in data)
        lead = max(distances)[1]
        points[lead] += 1

    return max(dist1)[0], max(points.values())


@timer
def main():
    with open("inputs/day14.txt") as f:
        data = [process_line(ln) for ln in f]

    print(solve_day14(data))


if __name__ == "__main__":
    main()
