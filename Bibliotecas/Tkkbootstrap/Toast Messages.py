import ttkbootstrap as tb
from ttkbootstrap.toast import ToastNotification

root = tb.Window(themename="superhero")
root.title("Treeview")
root.geometry("700x350")

def clicker():
    toast.show_toast()



toast = ToastNotification(title="My Toast Title", message="This is a toast message",
                          duration= 3000,
                          alert=True,
                          position=('sw'))

button = tb.Button(root, text="click me", command=clicker)
button.pack(pady=40)


root.mainloop()
