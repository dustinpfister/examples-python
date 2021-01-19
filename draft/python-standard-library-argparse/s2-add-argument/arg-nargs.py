import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--add', nargs=2)

args = parser.parse_args()

print(args.add);
