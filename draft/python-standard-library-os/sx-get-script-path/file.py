import os,sys
dir_current = os.getcwd()
dir_script = os.path.realpath(os.path.dirname(__file__))
dir_parent = os.path.dirname(dir_script)

# insert dir_parent
sys.path.insert(0, dir_parent)

print(dir_current)
print(dir_script)
print(dir_parent)

 


