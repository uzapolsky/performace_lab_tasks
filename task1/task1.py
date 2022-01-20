import argparse


def main(n, m):
    ind = 0
    seq = []
    while True:
        seq.append(str(ind + 1))
        ind += m - 1
        ind %= n
        if ind == 0:
            break
    print(''.join(seq))


parser = argparse.ArgumentParser()

parser.add_argument('n', nargs='?',
                    default=argparse.SUPPRESS, help='array length')
parser.add_argument('-n', dest='n', default=4)

parser.add_argument('m', nargs='?', default=argparse.SUPPRESS, help='step')
parser.add_argument('-m', dest='m', default=3)

args = parser.parse_args()
main(int(args.n), int(args.m))
