import tkinter as tk

class Tela:
    def clicou(self):
        print(self.verificar.get())
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('200x200')
        self.verificar = tk.IntVar()
        self.cbt1 = tk.Checkbutton(self.janela, text='Vasco')
        self.cbt2 =tk.Checkbutton(self.janela, text='Bayern',variable=self.verificar, command=self.clicou)

        self.cbt2.pack()
        self.cbt1.pack()


gui = tk.Tk()
Tela(gui)
gui.mainloop()