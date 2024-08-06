from tkinter import *


class App(Tk):

    def __init__(self):
        super().__init__()
    
        self.title('Teste opp with tkinter')
        self.iconbitmap('Bibliotecas\Tkinter\POO_tkinter\main02\potatos.ico')
        self.geometry('700x450')

        self.status = True

        self.my_label = Label(self, text='Hello World!', font=('Helvetica', 42))
        self.my_label.pack(pady=20)

        self.my_button = Button(self, text='Change Teext', command=self.change)
        self.my_button.pack(pady=20)

        MyFrame(self)

        self.mainloop()
    
    def change(self):

        if self.status:

            self.my_label.config(text='Goodbye World!')
            self.status = False

        else:

            self.my_label.config(text='Hello World!')
            self.status = True


class MyFrame(Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.pack(pady=20)

        self.my_button1 = Button(self, text='Change', command=parent.change)
        self.my_button2 = Button(self, text='Change', command=parent.change)
        self.my_button3 = Button(self, text='Change', command=parent.change)

        self.my_button1.grid(row=0, column=0, padx=10)
        self.my_button2.grid(row=0, column=1, padx=10)
        self.my_button3.grid(row=0, column=2, padx=10)


App()
