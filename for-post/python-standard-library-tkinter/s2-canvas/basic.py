import tkinter as tk
root = tk.Tk()
root.minsize(320, 240)

can = tk.Canvas(root, bg="white", height=300, width=300)
coord = 10, 10, 300, 300
can.create_arc(coord, start=90, extent=90, fill="red")

can.pack() 
root.mainloop() 