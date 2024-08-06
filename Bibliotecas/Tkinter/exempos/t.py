import os
import csv
import tkinter as tk
from tkinter import filedialog, messagebox

class CSVEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CSV Editor")

        self.directory_label = tk.Label(root, text="Diretório:")
        self.directory_label.pack()

        self.directory_entry = tk.Entry(root, width=50)
        self.directory_entry.pack()

        self.browse_button = tk.Button(root, text="Escolher Diretório", command=self.browse_directory)
        self.browse_button.pack()

        self.remove_file_label = tk.Label(root, text="Remover Arquivo:")
        self.remove_file_label.pack()

        self.remove_file_entry = tk.Entry(root, width=30)
        self.remove_file_entry.pack()

        self.remove_file_button = tk.Button(root, text="Remover Arquivo", command=self.remove_file)
        self.remove_file_button.pack()

        self.remove_lines_label = tk.Label(root, text="Remover Linhas (Intervalo):")
        self.remove_lines_label.pack()

        self.start_line_entry = tk.Entry(root, width=10)
        self.start_line_entry.pack(side=tk.LEFT)
        self.to_label = tk.Label(root, text="até")
        self.to_label.pack(side=tk.LEFT)
        self.end_line_entry = tk.Entry(root, width=10)
        self.end_line_entry.pack(side=tk.LEFT)
        self.remove_lines_button = tk.Button(root, text="Remover Linhas", command=self.remove_lines)
        self.remove_lines_button.pack()

    def browse_directory(self):
        directory = filedialog.askdirectory()
        self.directory_entry.delete(0, tk.END)
        self.directory_entry.insert(0, directory)

    def remove_file(self):
        file_to_remove = self.remove_file_entry.get()
        directory = self.directory_entry.get()

        if file_to_remove and directory:
            file_path = os.path.join(directory, file_to_remove)

            try:
                os.remove(file_path)
                messagebox.showinfo("Remoção de Arquivo", f"O arquivo '{file_to_remove}' foi removido com sucesso.")
            except Exception as e:
                messagebox.showerror("Erro", f"Ocorreu um erro ao remover o arquivo:\n{str(e)}")
        else:
            messagebox.showerror("Erro", "Por favor, insira um nome de arquivo e escolha um diretório.")

    def remove_lines(self):
        start_line = int(self.start_line_entry.get())
        end_line = int(self.end_line_entry.get())
        file_to_edit = self.remove_file_entry.get()
        directory = self.directory_entry.get()

        if file_to_edit and directory:
            file_path = os.path.join(directory, file_to_edit)

            try:
                with open(file_path, 'r') as file:
                    lines = file.readlines()

                with open(file_path, 'w') as file:
                    for i, line in enumerate(lines, start=1):
                        if i < start_line or i > end_line:
                            file.write(line)

                messagebox.showinfo("Remoção de Linhas", f"As linhas {start_line} até {end_line} foram removidas com sucesso.")
            except Exception as e:
                messagebox.showerror("Erro", f"Ocorreu um erro ao remover as linhas:\n{str(e)}")
        else:
            messagebox.showerror("Erro", "Por favor, insira um nome de arquivo, escolha um diretório e defina um intervalo válido.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CSVEditorApp(root)
    root.mainloop()
