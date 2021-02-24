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
# parse the arguments
args = parser.parse_args()

# using dice lib
set=dice.roll_set(count=int(args.count))
print(set)