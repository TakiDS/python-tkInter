import tkinter as tk

janela = tk.Tk()
janela.title('First Window with Tkinter')
janela.geometry('800x400')
janela.maxsize(400,500)
janela.resizable(width=False, height=False)

container = tk.Frame(janela, width=100, height=100, bg='green')# Declaração do frame com o parâmetro pai(janela)
container.pack(expand=True) #Adiciona o componente na janela


janela.mainloop()
