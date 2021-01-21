import tkinter as tk
import sys
import inspect

root=tk.Tk()

members=inspect.getmembers(root, inspect.ismethod)

# print out all methods and doc strings for them
# of the Tk Class
for m in members:
    print('\n\n\n')
    print(m[0], ' ( ', type(m[1]).__name__, ' ) ', m, sep='')
    print('********** ********** **********')
    print(m[1].__doc__)
    
sys.exit(0)
    
