# Open file with Filedialog 

É uma maneira simples de vc navegar pelos arquivos do computador e selecionar diretórios ou arquivos de interesse.

Utilizamos um módulo da bibliteca tkinter chamada filedialog. Ela possui alguns métodos expecíficos que limitam o que vc pode selecionar ou não. Temos, por exemplo, o askopenfilenames( ), que selciona arquivos; o askdirectory( ) que dexa vc selecionar apenas uma pasta. 

Esses são apenas alguns. Pesquise na documentação para ver o que esse módulo tem de interessante.

```Python
from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("FileDialog")

root.filename = filedialog.askopenfilenames(initialdir=r"C:\ " , title="Select files", filetypes=(("png files", "*.png"), ("all files", "*.*")))

root.mainloop()
```

```Python
from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("FileDialog")

def open():

    root.filename = filedialog.askopenfilenames(initialdir=r"C:\ " , title="Select files", filetypes=(("png files", "*.png"), ("all files", "*.*")))


bnt = Button(root, text="Open File", command=open).pack()

root.mainloop()
```