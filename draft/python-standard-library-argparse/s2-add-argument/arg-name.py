import argparse

parser = argparse.ArgumentParser()

# set one or more names for the argument with the first, or more positional arguments
# when calling add_argumnet
parser.add_argument('--foo', '-f',
                    dest='foo',
                    action='store_true',
                    default=False)

# parse the arguments
args = parser.parse_args()
print(args.foo);
