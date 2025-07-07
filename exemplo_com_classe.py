import tkinter as tk

class MinhaTela:
    def __init__(self, d):
        self.janela = d
        self.janela.title('First Window with Tkinter')
        self.janela.geometry('800x400')
        self.janela.maxsize(400, 500)
        self.janela.resizable(width=False, height=False)

        container = tk.Frame(self.janela, width=100, height=100,bg='green')  # Declaração do frame com o parâmetro pai(janela)
        container.pack(expand=True)  # Adiciona o componente na janela

        self.nome = tk.Label(container, text='Marcos')
        self.email = tk.Label(self.janela, text='Aiulo@gmial')
        self.nome.pack()
        self.email.pack()

gui = tk.Tk()
minhatela = MinhaTela(gui)
gui.mainloop()






