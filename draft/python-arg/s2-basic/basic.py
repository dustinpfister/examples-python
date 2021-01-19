import argparse

# create a parser
parser = argparse.ArgumentParser(description='Basic argparse example.')

# have at least one argument
parser.add_argument('--foo',
                    dest='mode',
                    action='store_true',
                    default=False,
                    help='set foo mode true (default: False)')

# parse the arguments
args = parser.parse_args()

# use the arguments
if(args.mode):
    print('FOO MODE!')
else:
    print('bar mode')
