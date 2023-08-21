# Scrolled text and scrolled frame

Scrolled text example

```Python
import ttkbootstrap as tb
from ttkbootstrap.scrolled import ScrolledText

root = tb.Window(themename="solar")
root.title("Scroll text")
root.geometry("500x350")

text = ScrolledText(root, height=20, width=110, bootstyle="success", autohide=True, hbar=False)
text.pack(pady=15)

root.mainloop()
```

Scrolled frame example

```Python
import ttkbootstrap as tb
from ttkbootstrap.scrolled import ScrolledText

root = tb.Window(themename="solar")
root.title("Scroll text")
root.geometry("500x350")

frame = ScrolledFrame(root, autohide=False, bootstyle="success")
frame.pack(padx=15, pady=15, fill="both", expand="yes")

for x in range(21):
    tb.Button(frame, bootstyle="info", text=f"click me {x}").pack(pady=10)

root.mainloop()
```
