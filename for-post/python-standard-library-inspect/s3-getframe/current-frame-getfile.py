import inspect
import os

frame=inspect.currentframe()
file=inspect.getfile(frame)
folder=os.path.dirname(file)
filename=os.path.basename(file)

print(folder);
print(filename);