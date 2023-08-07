# Frames

Nada mais é que um frame dentro do janela onde 
você pode organizar seus Widgets.

```Python
root = tb.Window(themename="superhero")

root.title("Date entry")
root.geometry("500x350")

frame = tb.Frame(root, bootstyle="light")
frame.pack(pady=40)

entry = tb.Entry(frame, font=("Helvetica", 18))
entry.pack(pady=20, padx=20)

```

Se quiser o frame sendo transparente, utilize o do tkinter mesmo, não o do ttkbootstrap.
