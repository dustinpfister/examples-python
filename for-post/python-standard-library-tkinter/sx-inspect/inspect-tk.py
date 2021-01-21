import tkinter as tk
import inspect

root=tk.Tk()

members=inspect.getmembers(root)

for m in members:
    print(m[0])