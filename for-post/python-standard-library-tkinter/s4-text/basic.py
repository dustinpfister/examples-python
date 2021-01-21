import tkinter as tk
root = tk.Tk()
root.minsize(640, 480)

# create a text widget
text = tk.Text(root, width=60, height=25)

# insert some start text
text.insert(2.0, 'hello world\n')
text.insert(1.0, '1234\n')
text.insert(2.6, 'cruel ')

text.pack() 
root.mainloop() 