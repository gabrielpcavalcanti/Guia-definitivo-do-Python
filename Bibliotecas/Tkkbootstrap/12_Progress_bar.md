# Progress Bar

É uma barra de progresso. Vamos ver o que da para fazer com ela.

```Python
from tkinter import *
import ttkbootstrap as tb
import time

def increment():
    #progress_bar.step(20)
    progress_bar['value'] += 20

    if progress_bar['value'] <=100:
        label.config(text=progress_bar['value'])

def start():
    progress_bar.start(10)

def stop():
    progress_bar.stop()

def auto():
    for x in range(5):
        progress_bar['value'] += 20
        label.config(text=progress_bar["value"])
        root.update_idletasks()
        time.sleep(1) 

    
root = tb.Window(themename="solar")
root.title("Progress bar")
root.geometry("500x350")

progress_bar = tb.Progressbar(root, bootstyle="danger striped",
                              maximum=100,
                              mode="determinate",
                              length=300,
                              value=0)
progress_bar.pack(pady=20)

frame = tb.Frame(root)
frame.pack(pady=20)

button = tb.Button(frame, text="Increment 20", bootstyle="info", command=increment)
button.grid(column=0, row=0, padx=10)

button2 = tb.Button(frame, text="Start", bootstyle="info", command=start)
button2.grid(column=1, row=0, padx=10)

button3 = tb.Button(frame, text="Stop", bootstyle="info", command=stop)
button3.grid(column=2, row=0, padx=10)

button4 = tb.Button(frame, text="Auto", bootstyle="info", command=auto)
button4.grid(column=3, row=0, padx=10)

label = tb.Label(root, text="", font=("helvetica", 18))
label.pack(pady=20)

root.mainloop()

```
