import argparse

parser = argparse.ArgumentParser()

# default action is 'store' whioch will just store any given value for
# the argument. If no default is set then the default value for the
# argument will be None. The default dist for the argument will be the name
# of the argument
parser.add_argument('--foo')

args = parser.parse_args()
print(args.foo);
