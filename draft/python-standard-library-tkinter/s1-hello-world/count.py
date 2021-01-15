import tkinter as tk

root = tk.Tk()

def helloCallBack():
   print('hello')

B = tk.Button(root, text ="Hello", command = helloCallBack)

B.pack()
root.mainloop()