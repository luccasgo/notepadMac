import tkinter as tk
from tkinter import filedialog, messagebox
import os

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Bloco de Anotações")
        self.root.geometry("800x600")
        self.root.attributes('-topmost', True)
        
     
        self.text_area = tk.Text(self.root, wrap='word')
        self.text_area.pack(expand=1, fill='both')
        
    
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)
        
  
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Arquivo", menu=self.file_menu)
        
        self.file_menu.add_command(label="Novo", command=self.new_file)
        self.file_menu.add_command(label="Abrir", command=self.open_file)
        self.file_menu.add_command(label="Salvar", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Sair", command=self.root.quit)
        

        self.transparency_scale = tk.Scale(self.root, from_=20, to=100, orient='horizontal', label='Transparência', command=self.set_transparency)
        self.transparency_scale.pack(fill='x')
        self.transparency_scale.set(100)
        
        self.file_path = None
        self.last_directory = None
    
    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.file_path = None
        self.root.title("Bloco de Anotações - Novo")

    def open_file(self):
        self.file_path = filedialog.askopenfilename(defaultextension=".txt",
                                                    filetypes=[("Todos os arquivos", "*.*"), 
                                                               ("Arquivos de texto", "*.txt")],
                                                    initialdir=self.last_directory)
        if self.file_path:
            with open(self.file_path, 'r') as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(1.0, file.read())
            self.root.title(f"Bloco de Anotações - {os.path.basename(self.file_path)}")
            self.last_directory = os.path.dirname(self.file_path)

    def save_file(self):
        if not self.file_path:
            self.file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                          filetypes=[("Todos os arquivos", "*.*"), 
                                                                     ("Arquivos de texto", "*.txt")],
                                                          initialdir=self.last_directory)
        if self.file_path:
            with open(self.file_path, 'w') as file:
                file.write(self.text_area.get(1.0, tk.END))
            self.root.title(f"Bloco de Anotações - {os.path.basename(self.file_path)}")
            self.last_directory = os.path.dirname(self.file_path)
    
    def set_transparency(self, value):
        self.root.attributes('-alpha', float(value) / 100)

if __name__ == "__main__":
    root = tk.Tk()
    notepad = Notepad(root)
    root.mainloop()
