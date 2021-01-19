import argparse

parser = argparse.ArgumentParser(description='Basic argparse boolean example.')

# sore_const action
parser.add_argument('--degree', '-d',
                    action='store_const',
                    dest='scale',
                    const=360.00,
                    default=6.28,
                    help='set scale to 360')

parser.add_argument('--angle', '-a',
                    dest='angle',
                    action='store',
                    default=0,
                    help='an angle value')

args = parser.parse_args()
per = float(args.angle) / args.scale;
print('per=' + str(per), 'scale=' + str(args.scale), 'angle=' + str(args.angle))
