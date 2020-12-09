import re
from collections import defaultdict

from utils import timer


MOLECULE = "CRnSiRnCaPTiMgYCaPTiRnFArSiThFArCaSiThSiThPBCaCaSiRnSiRnTiTiMgArPBCaPMgYPTiRnFArFArCaSiRnBPMgArPRnCaPTiRnFArCaSiThCaCaFArPBCaCaPTiTiRnFArCaSiRnSiAlYSiThRnFArArCaSiRnBFArCaCaSiRnSiThCaCaCaFYCaPTiBCaSiThCaSiThPMgArSiRnCaPBFYCaCaFArCaCaCaCaSiThCaSiRnPRnFArPBSiThPRnFArSiRnMgArCaFYFArCaSiRnSiAlArTiTiTiTiTiTiTiRnPMgArPTiTiTiBSiRnSiAlArTiTiRnPMgArCaFYBPBPTiRnSiRnMgArSiThCaFArCaSiThFArPRnFArCaSiRnTiBSiThSiRnSiAlYCaFArPRnFArSiThCaFArCaCaSiThCaCaCaSiRnPRnCaFArFYPMgArCaPBCaPBSiRnFYPBCaFArCaSiAl"


def process_line(ln):
    items = ln.split(" => ")
    return tuple(items)


@timer
def part1(data):
    molecules = set()
    molecule = re.findall('[A-Z][a-z]*', MOLECULE)
    for i, c in enumerate(molecule):
        for new in data[c]:
            molecule[i] = new
            molecules.add("".join(molecule))
        molecule[i] = c
    return len(molecules)


@timer
def part2(data):
    molecule = MOLECULE
    count = 0
    while molecule != 'e':
        for trans in data:
            if trans[0] in molecule:
                count += molecule.count(trans[0])
                molecule = molecule.replace(trans[0], trans[1])
                break

    return count


def solve_day19(data1, data2):
    result1 = part1(data1)
    result2 = part2(data2)
    return result1, result2


@timer
def main():
    with open("inputs/day19.txt") as f:
        data = [process_line(ln.strip()) for ln in f]

    data1 = defaultdict(list)
    for k, v in data:
        data1[k].append(v)

    data2 = sorted([(v, k) for k, v in data], key=lambda x: -sum(1 for c in x[0] if c.isupper()))
    print(solve_day19(data1, data2))


if __name__ == "__main__":
    main()
