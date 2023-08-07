# Meters

É uma barra de progresso circular, onde vc pode configurar muita, mas muita coisa mesmo. Veja abaixo um exemplo de uso e observe as opções disponíveis para esse Widget.

```Python
from tkinter import *
import ttkbootstrap as tb

global counter
counter = 20

def up():
    meter.step(10)

def down():
    meter.step(-10)

def clicker_5():
    global counter
    if counter <= 100:
        meter.configure(amountused=counter)
        counter += 5
        button_5.configure(text=f"Click Me {meter.amountusedvar.get()}")

root = tb.Window(themename='solar')

root.title("Meters")
root.geometry("550x750")

meter = tb.Meter(root, bootstyle='danger', subtext='Tkinter Learned',
                 interactive=True, textright="%", #textleft="$"
                 metertype="full", # also can be semi,
                  stripethickness=20,
                  metersize=200,
                  padding=50,
                  amountused=0,
                  amounttotal=100,
                  subtextstyle="success")
meter.pack(pady=50)

button_5 = tb.Button(root, text='click me', command= clicker_5)
button_5.pack(pady=20)

button_up = tb.Button(root, text='step up', command= up)
button_up.pack(pady=20)

button_down = tb.Button(root, text='step down', command= down)
button_down.pack(pady=20)


root.mainloop()

```