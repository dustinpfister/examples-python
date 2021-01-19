import argparse

parser = argparse.ArgumentParser()

# default action is 'store' whioch will just store any given value for
# the argument. If no default is set then the default value for the
# argument will be None. The default dist for the argument will be the name
# of the argument

parser.add_argument('--foo')

# here is anoher argument, with values set to what the defaults are
parser.add_argument('--bar',
                    action='store',
                    default=None,
                    dest='bar')

args = parser.parse_args()
print(args.foo);
print(args.bar);
