from utils import timer
from operator import and_, or_, lshift, rshift, inv


ops = {"AND": and_, "OR": or_, "LSHIFT": lshift, "RSHIFT": rshift, "NOT": inv, "ID": lambda x: x}


def get_inputs(data, cache, inputs):
    ins = []
    for i in inputs:
        if isinstance(i, int):
            ins.append(i)
        else:
            if i not in cache:
                cache[i] = applyop(data, cache, data[i]['op'], data[i]['input'])
            ins.append(cache[i])

    return ins


def applyop(data, cache, op, inputs):
    if all(isinstance(x, int) for x in inputs):
        return ops[op](*inputs)
    else:
        ins = get_inputs(data, cache, inputs)
        return ops[op](*ins)


def process_line(ln):
    items = ln.split()
    key = items[-1]
    info = {}
    if items[0] == 'NOT':
        info['op'] = 'NOT'
        info['input'] = [items[1]]
    elif len(items) == 3:
        info['op'] = 'ID'
        info['input'] = [items[0]]
    else:
        info['op'] = items[1]
        info['input'] = [items[0], items[2]]

    for idx, it in enumerate(info['input']):
        try:
            info['input'][idx] = int(it)
        except ValueError:
            pass

    return key, info


@timer
def solve_part1(data):
    a = data['a']
    cache = {}
    return applyop(data, cache, a['op'], a['input'])


@timer
def solve_part2(data, part1):
    data['b'] = {'op': 'ID', 'input': [part1]}
    a = data['a']
    cache = {}
    return applyop(data, cache, a['op'], a['input'])


def solve_day7(data):
    part1 = solve_part1(data)
    part2 = solve_part2(data, part1)

    return part1, part2


def main():
    with open("inputs/day7.txt") as f:
        data = dict(process_line(line.strip()) for line in f)

    print(data['a'])
    print(data['lw'])
    print(solve_day7(data))


if __name__ == "__main__":
    main()
