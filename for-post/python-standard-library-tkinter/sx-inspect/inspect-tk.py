import tkinter as tk
import sys
import inspect

root=tk.Tk()

members=inspect.getmembers(root, inspect.ismethod)

for m in members:
    method = m[0]
    print(method)
    
sys.exit(0)
    
