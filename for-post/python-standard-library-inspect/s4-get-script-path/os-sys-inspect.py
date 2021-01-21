import os,sys,inspect

# CURRENT WORKING DIR
# can be obtained with os.getcwd()
dir_current = os.getcwd()

# DIR OF THIS SCRIPT
# get current frame object with inspect.current frame,
# the frame object can then be passed to inspect.getFile
# that path can then be passed to os.path.abspath, and os.path.dirname
frame_obj = inspect.currentframe()
path_script = inspect.getfile(frame_obj)
dir_script = os.path.dirname(os.path.abspath(path_script))

# DIR OF PARENT FOLDER OF THIS SCRIPT
# once I have the dir to the script I can just pass that to os.path.dirname
# to go down one level
dir_parent = os.path.dirname(dir_script)

# INSERT
# the sys.path list is a list of dirs where python
# will look for modules. I can then insert the parent folder
# to make python look there for any additional modules
# I might like to import
sys.path.insert(0, dir_parent)

print(dir_current)
print(path_script)
print(dir_script)
print(dir_parent)

 


