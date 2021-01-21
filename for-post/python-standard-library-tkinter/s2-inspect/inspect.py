import tkinter as tk
import inspect

members=inspect.getmembers(tk)

for m in members:
    print('')
    print(m[0], ' ( ', type(m[1]).__name__, ' ) ', m, sep='')
    print('********** ********** **********')
    print(m[1].__doc__)