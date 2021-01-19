import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--foo')

# parse the arguments
args = parser.parse_args()

print(args.foo);

