import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('200x200')
        self.lbl_login = tk.Label(self.janela, text='login').pack()
        self.ent_login = tk.Entry(self.janela, width=20).pack()

        self.lbl_senha = tk.Label(self.janela, text='Senha:').pack()
        self.ent_senha = tk.Entry(self.janela, width=20, show='*').pack()

        self.btn_confi = tk.Button(self.janela, text='Enviar').pack()

gui = tk.Tk()
Tela(gui)
gui.mainloop()