import argparse, os,sys,inspect
# insert lib folder
dir_current = os.getcwd()
dir_script = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.insert(0, dir_script + '/lib')
# import dice from lib folder
import dice
 
# create a argument parser
parser = argparse.ArgumentParser(description='Basic argparse example.')
 
# arguments
parser.add_argument('--count',
                    dest='count',
                    action='store',
                    default=1,
                    help='Set the count of dice (default: 1)')
parser.add_argument('--sides',
                    dest='sides',
                    action='store',
                    default='6',
                    help='sides list (default: [6])')
parser.add_argument('--default_sides',
                    dest='default_sides',
                    action='store',
                    default=6,
                    help='default side count (default: 6)')
# parse the arguments
args = parser.parse_args()

sides = args.sides.split(',');

# using dice lib
set=dice.roll_set( count = int(args.count),  sides = sides )
print(set)