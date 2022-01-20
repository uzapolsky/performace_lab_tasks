import argparse


def in_square_check(cx, cy, dx, dy, r):
    sq_length = (dx - cx) ** 2 + (dy - cy) ** 2
    sq_rad = r ** 2
    if sq_length > sq_rad:
        return 2
    elif sq_length < sq_rad:
        return 1
    return 0


def main(file1, file2):

    with open(file1, 'r') as f1:
        center_x, center_y = map(int, f1.readline().split())
        radius = int(f1.readline())

    with open(file2, 'r') as f2:
        for dot in f2.readlines():
            dot_x, dot_y = map(int, dot.split())
            print(in_square_check(center_x, center_y, dot_x, dot_y, radius))


parser = argparse.ArgumentParser()
parser.add_argument('file1', help='filepath to circle desc file')
parser.add_argument('file2', help='filepath to dots coordinates file')
args = parser.parse_args()
main(args.file1, args.file2)
