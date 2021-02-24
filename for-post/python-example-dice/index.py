import os,sys,inspect
dir_current = os.getcwd()
dir_script = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# insert lib folder
sys.path.insert(0, dir_script + '/lib')
import dice
# using dice lib
set=dice.roll_set(count=4)
print(set)