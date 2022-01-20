import argparse
from statistics import median


def main(file):
    with open(file, 'r') as f:
        nums = list(map(int, f.readlines()))
    med = int(round(median(nums)))
    steps = 0
    for n in nums:
        steps += abs(n - med)
    print(steps)


parser = argparse.ArgumentParser()
parser.add_argument('file', help='filepath to nums file')
args = parser.parse_args()
main(args.file)
