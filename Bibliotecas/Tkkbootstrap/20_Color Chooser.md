# Color chooser

É um seletor de cores. bem legal.

```Python
import ttkbootstrap as tb
from ttkbootstrap.dialogs.colorchooser import ColorChooserDialog

root = tb.Window(themename="superhero")

root.title("Color Chooser")
root.geometry("500x350")

def cc():
    my_color = ColorChooserDialog()
    my_color.show()
    colors = my_color.result
    label.config(text=colors.hex) #rgb rsl
    root.configure(background=colors.hex)

button = tb.Button(root, text="click me", bootstyle="danger", command=cc)
button.pack(pady=40)

label = tb.Label(root, text="", font=("Helvetica", 18))
label.pack(pady=10)

root.mainloop()

```
