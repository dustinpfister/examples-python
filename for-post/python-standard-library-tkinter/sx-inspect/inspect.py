import tkinter as tk
import inspect

members=inspect.getmembers(tk)

for m in members:
    print(m[0])