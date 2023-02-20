from tkinter import *

root = Tk()

root.title("Simple Calculator")

def win_size():
    #Tamanho inicial da janela
    largura_janela = 295
    altura_janela = 430

    # Resolução do sistema
    largura_screen = root.winfo_screenwidth()
    altura_screen = root.winfo_screenheight()

    # Posição da janela
    posx = largura_screen / 2 - largura_janela / 2
    posy = altura_screen / 2 - altura_janela / 2

    # Geometria 
    root.geometry("{}x{}+{}+{}".format(int(largura_janela), int(altura_janela), int(posx), int(posy)))

def button_click(number):

    current = e.get()
    e.delete(0,END)
    e.insert(0, str(current) + str(number))

def button_clear():

    e.delete(0, END)


def button_add():

    first_num = e.get()
    global f_num
    global math
    math = "add"
    f_num = int(first_num)
    e.delete(0,END)

def button_sub():

    first_num = e.get()
    global f_num
    global math
    math = "sub"
    f_num = int(first_num)
    e.delete(0,END)

def button_mult():

    first_num = e.get()
    global f_num
    global math
    math = "mult"
    f_num = int(first_num)
    e.delete(0,END)

def button_div():

    first_num = e.get()
    global f_num
    global math
    math = "div"
    f_num = int(first_num)
    e.delete(0,END)

def button_equal():
    
    second_num = e.get()
    e.delete(0,END)

    if math == 'add':
        e.insert(0,f_num + int(second_num))
    
    if math == 'sub':
        e.insert(0,f_num - int(second_num))
    
    if math == 'mult':
        e.insert(0,f_num * int(second_num))
    
    if math == 'div':
        e.insert(0,f_num / int(second_num))


win_size()

e = Entry(root, width=35, borderwidth=2)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

btn_1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_click(1))
btn_2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_click(2))
btn_3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_click(3))
btn_4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_click(4))
btn_5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_click(5))
btn_6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_click(6))
btn_7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_click(7))
btn_8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_click(8))
btn_9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_click(9))
btn_0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_click(0))

btn_add = Button(root, text='+', padx=39, pady=20, command=button_add)
btn_sub = Button(root, text='-', padx=41, pady=20, command=button_sub)
btn_mult = Button(root, text='*', padx=40, pady=20, command=button_mult)
btn_div = Button(root, text='/', padx=41, pady=20, command=button_div)


btn_equal = Button(root, text='=', padx=88, pady=20, command=button_equal)
btn_clear = Button(root, text='Clear', padx=78, pady=20, command=button_clear)

btn_1.grid(row=3, column=0)
btn_2.grid(row=3, column=1)
btn_3.grid(row=3, column=2)

btn_4.grid(row=2, column=0)
btn_5.grid(row=2, column=1)
btn_6.grid(row=2, column=2)

btn_7.grid(row=1, column=0)
btn_8.grid(row=1, column=1)
btn_9.grid(row=1, column=2)

btn_0.grid(row=4, column=0)

btn_add.grid(row=5, column=0)
btn_sub.grid(row=6, column=0)
btn_mult.grid(row=6, column=1)
btn_div.grid(row=6, column=2)

btn_equal.grid(row=5, column=1,columnspan=2)
btn_clear.grid(row=4, column=1, columnspan=2)


root.mainloop()
