# Entry boxes

Uma caixa onde vc pode escrever coisas, como o própio nome diz, uma caixa de entrada.

```Python
entry = tb.Entry(root, bootstyle="success",
                font=("Helvetica", 18), 
                foreground="blue",
                width=15, 
                show="*")

entry.pack(pady=50)
```