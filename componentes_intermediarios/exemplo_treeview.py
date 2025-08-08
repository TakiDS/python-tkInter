import tkinter as tk
from tkinter import ttk

class Tela:
    def  __init__(self, master):
        self.janela = master


        colunas = ['nome', 'cpf', 'email']
        self.tvw = ttk.Treeview(self.janela, height=5, columns=colunas, show='headings')
        #Configurar o cabeça
        self.tvw.heading('nome',text='NOME')
        self.tvw.heading('cpf', text='CPF')
        self.tvw.heading('email', text='EMAIL')

        self.tvw.insert('', 'end', values=('Limeira', '0000000000', 'Limeira@ufac.com.br'))
        self.tvw.insert('', 'end', values=('Adolfo', '0000000000', 'Limeira@ufac.com.br'))
        self.tvw.insert('', 'end', values=('Miguel', '0000000000', 'Limeira@ufac.com.br'))
        self.tvw.insert('', 'end', values=('Katarina', '0000000000', 'Limeira@ufac.com.br'))
        self.tvw.insert('', 'end', values=('Adolfo', '0000000000', 'Limeira@ufac.com.br'))
        self.tvw.insert('', 'end', values=('Miguel', '0000000000', 'Limeira@ufac.com.br'))
        self.tvw.insert('', 'end', values=('Katarina', '0000000000', 'Limeira@ufac.com.br'))

        self.brl = ttk.Scrollbar(master,command=self.tvw.yview)
        self.brl.grid(row=0, column=1, sticky='ns')
        self.tvw.configure(yscrollcommand=self.brl.set)
        self.tvw.grid(row=0, column=0)
        self.centralizar(self.janela)

    def centralizar(self, master):
        # Criando uma forma centralizar a janela
        largura_monitor = self.janela.winfo_screenwidth()
        altura_monitor = self.janela.winfo_screenheight()
        master.update_idletasks()

        largura_janela= master.winfo_width()
        altura_janela= master.winfo_height()
        x = largura_monitor // 2 - largura_janela //2
        y = altura_monitor //2 - altura_janela//2
        master.geometry(f'{largura_janela}x{altura_janela}+{x}+{y}')
        print(largura_janela)

gui = tk.Tk()
Tela(gui)
gui.mainloop()