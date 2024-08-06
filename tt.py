import tkinter as tk
from ttkbootstrap import Style

root = tk.Tk()

style = Style(theme='flatly')
style.configure('TButton', font=('Helvetica', 12))

button = tk.Button(root, text='Click Me', command=lambda: print('Button clicked!'))
button.pack()

root.mainloop()