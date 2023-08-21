import ttkbootstrap as tb
from ttkbootstrap.dialogs import Messagebox

root = tb.Window(themename="superhero")

root.title("Message box")
root.geometry("500x350")

def clicker():

    # temos outros tipo de message box: ok, okcancel, show_info, show_error, show_question,
    # show_warning, yesnocancel, retrycancel
    mb = Messagebox.yesno("Display Some message Here", "Here is the title")

    label.config(text=f"you clicked {mb}")


button = tb.Button(root, text="click me", bootstyle="danger", command=clicker)
button.pack(pady=40)

label = tb.Label(root, text='', font=("helvetica", 18))
label.pack(pady=20)

root.mainloop()
