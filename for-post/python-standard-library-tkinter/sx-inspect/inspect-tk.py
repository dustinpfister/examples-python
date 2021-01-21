import tkinter as tk
import sys
import inspect

root=tk.Tk()

members=inspect.getmembers(root, inspect.ismethod)

# print out all methods and doc strings for them
# of the Tk Class
for m in members:
    method = m[0]
    print('')
    print(method)
    print('********** ********** **********')
    print(method.__doc__)
    
sys.exit(0)
    
