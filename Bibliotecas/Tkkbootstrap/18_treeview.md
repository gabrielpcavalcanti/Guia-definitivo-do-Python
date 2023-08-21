# Treeview

É como se fosse uma tabela com linhas e colunas, mas um pouco diferente. Veja como aplicar num exemplo.

```Python
from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")
root.title("Treeview")
root.geometry("700x350")

columns = ("first_name", "last_name", "email")

tree = tb.Treeview(root, bootstyle="success", columns=columns, show="headings")
tree.pack(pady=20)

tree.heading("first_name", text="First Name")
tree.heading("last_name", text="Last Name")
tree.heading("email", text="Email Address")

contacts = []

for n in range(1,20):
    contacts.append((f"First {n}", f"Last {n}", f"email{n}@address.com"))

for contact in contacts:
    tree.insert("", END, values=contact)

root.mainloop()

```
