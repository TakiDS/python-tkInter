import tkinter as tk

gui = tk.Tk()

class MinhaTela:
    def __init__(self,gui):
        self.janela = gui
        self.janela.title("Tela")
        self.janela.geometry('300x200')

        self.lbl_nome = tk.Label(container, text='nome',bg='blue')
        self.lbl_nome.pack()
        self.ent_nome = tk.Entry(container, width=20)
        self.ent_nome.pack()
        self.lbl_dataNascimento = tk.Label(container, text='Data de Nascimento')
        self.lbl_dataNascimento.pack()
        self.ent_dataNascimento = tk.Entry(container)
        self.ent_dataNascimento.pack()
        self.btn_enviar = tk.Button(container, text='Enviar',command=self.CalcData).pack()
        self.lbl_res = tk.Label(container)
        self.lbl_res.pack()

    def CalcData(self):
        dataEnt = self.ent_dataNascimento.get()
        if "/" in dataEnt:


            date = dataEnt.split("/")

            dataAtual = [8,7,2025]
            dias = dataAtual[0]-int(date[0])
            mes = dataAtual[1] - int(date[1])
            ano = dataAtual[2] - int(date[2])
            self.lbl_res.config(text=f'Anos: {abs(ano)},  os meses: {abs(mes)}, e os dias: {abs(dias)} ou {(ano*365)+dias} dias')

container = tk.Frame(gui, width=100, height=100, bg='green')
container.pack(expand=True)

MinhaTela(gui)
gui.mainloop()

