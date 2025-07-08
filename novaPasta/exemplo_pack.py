import tkinter as tk

class Tela:
    def __init__(self,master):
        self.janela = master
        self.janela.geometry('500x500')
        lbl1 = tk.Label(self.janela, text='label 1', fg='white', bg='yellow')
        lbl1.pack(fill='x', expand=True, side='left')
        lbl2 = tk.Label(self.janela, text='label 2', fg='white', bg='blue')
        lbl2.pack(fill='y', expand=True)

gui = tk.Tk()
Tela(gui)
gui.mainloop()