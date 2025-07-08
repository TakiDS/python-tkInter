import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('200x200')
        self.lbl_login = tk.Label(self.janela, text='login')
        self.lbl_login.grid(row=0, column=0)
        self.ent_login = tk.Entry(self.janela, width=20)
        self.ent_login.grid(row=0, column=1)

        self.lbl_senha = tk.Label(self.janela,text='Senha:')
        self.lbl_senha.grid(row=1, column=0)

        self.ent_senha = tk.Entry(self.janela, width=20, show='*')
        self.ent_senha.grid(row=1, column=1)
        self.btn_confi = tk.Button(self.janela, text='Enviar')
        self.btn_confi.grid(row=2, column=1, stick='we',columnspan=1)

gui = tk.Tk()
Tela(gui)
gui.mainloop()