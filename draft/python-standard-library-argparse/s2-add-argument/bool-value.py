import argparse

# create a parser
parser = argparse.ArgumentParser(description='Basic argparse boolean example.')

# a bool argument can be created by using the 'store_true', or 'store_false' value for
# the action argument of the add_argument method. If for example the 'store_true' action
# is used, then it would make sense to set the default argument to False
parser.add_argument('--foo',
                    dest='foomode',
                    action='store_true',
                    default=False,
                    help='set foomode true (default: False)')

# parse the arguments
args = parser.parse_args()
# use the arguments
if(args.foomode):
    print('FOO MODE!')
else:
    print('bar mode')
