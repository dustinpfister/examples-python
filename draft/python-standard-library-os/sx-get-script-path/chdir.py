import os,sys,inspect

# ch to root
os.chdir('/');

# now getting dir values
dir_current = os.getcwd()
dir_script = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
dir_parent = os.path.dirname(dir_script)

# insert dir_parent
sys.path.insert(0, dir_parent)

print(dir_current)
print(dir_script)
print(dir_parent)

 


