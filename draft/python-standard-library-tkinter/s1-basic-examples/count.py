import tkinter as tk

root = tk.Tk()
btn_text = tk.StringVar()
btn_text.set('0')

def update_btn_text():
    n = int(btn_text.get())
    n = n + 1
    btn_text.set(str(n))

btn = tk.Button(root, textvariable=btn_text, command=update_btn_text)
btn.pack()

root.mainloop()