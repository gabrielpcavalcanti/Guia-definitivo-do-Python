from tkinter import *
import ttkbootstrap as tb

def start():
    gauge.start()

def stop():
    gauge.stop()

def incre():
    gauge.step(10)

root = tb.Window(themename="flatly")

root.title("Floodgauge")
root.geometry("500x550")

gauge = tb.Floodgauge(root, bootstyle="success",
                      font=("Helvetica",18),
                      mask="Pos: {}%",
                      maximum=100,
                      orient="horizontal",
                      value=0)

gauge.pack(pady=50, fill=X, padx=20)

start_bt = tb.Button(root, text="Start", bootstyle="danger outline", command=start)
start_bt.pack(pady=20)

stop_bt = tb.Button(root, text="Stopt", bootstyle="danger outline", command=stop)
stop_bt.pack(pady=20)

inc_bt = tb.Button(root, text="increment", bootstyle="danger outline", command=incre)
inc_bt.pack(pady=20)

root.mainloop()
