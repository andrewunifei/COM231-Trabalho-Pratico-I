import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.constants import LEFT

class MyGUI:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.geometry('550x275')
        self.janela.eval('tk::PlaceWindow . center')

        # Cria dois frames, um para os checkbuttons
        # e outro para o botão
        self.frameRight = tk.Frame(self.janela)
        self.frameLeft = tk.Frame(self.janela)

        
        # Cria 3 objetos IntVar para usar com os checkbuttons    
        self.cbVar1 = tk.IntVar()
        self.cbVar2 = tk.IntVar()
        self.cbVar3 = tk.IntVar()
        self.cbVar4 = tk.IntVar()
        self.cbVar5 = tk.IntVar()
        self.cbVar6 = tk.IntVar()
        self.box1 = tk.StringVar()
        self.box2 = tk.StringVar()

        # Ajusta os IntVar objetos para 0
        self.cbVar1.set(0)
        self.cbVar2.set(0)
        self.cbVar3.set(0)
        self.cbVar4.set(0)
        self.cbVar5.set(0)
        self.cbVar6.set(0)
        
        # FrameLeft
        self.txt01 = tk.Label(self.frameLeft, text='Selecione a tabela: ')
        self.txt01.grid(column=0, row=0)

        self.combobox1 = ttk.Combobox(self.frameLeft, textvariable=self.box1)
        self.combobox1.grid(column=0, row=1)

        self.txt000 = tk.Label(self.frameLeft, text=' ')
        self.txt000.grid(column=0, row=2)

        self.listbox = tk.Listbox(self.frameLeft)
        self.listbox.grid(column=0, row=3)

        # FrameRight
        self.txt1 = tk.Label(self.frameRight, text='Filtros')
        self.txt1.grid(column=1, row=0, sticky='W')

        self.cb1 = tk.Checkbutton(self.frameRight, text='Data de ', variable=self.cbVar1)
        self.cb1.grid(column=1, row=1, sticky='W')

        self.inputData1 = tk.Entry(self.frameRight, width=10)
        self.inputData1.grid(column=2, row=1, sticky='W')

        self.txt2 = tk.Label(self.frameRight, text=' até ')
        self.txt2.grid(column=3, row=1, sticky='W')

        self.inputData2 = tk.Entry(self.frameRight, width=10)
        self.inputData2.grid(column=4, row=1, sticky='W')

        self.cb2 = tk.Checkbutton(self.frameRight, text='Limite de linhas ', variable=self.cbVar2)
        self.cb2.grid(column=1, row=2, sticky='W')

        self.inputData3 = tk.Entry(self.frameRight, width=10)
        self.inputData3.grid(column=2, row=2, sticky='W')

        self.txt00 = tk.Label(self.frameRight, text=' ')
        self.txt00.grid(column=0, row=3, sticky='W')

        self.txt3 = tk.Label(self.frameRight, text='Ordenação ')
        self.txt3.grid(column=1, row=4, sticky='W')

        self.combobox2 = ttk.Combobox(self.frameRight, width=10, textvariable=self.box2)
        self.combobox2.grid(column=2, row=4, sticky='W')

        self.txt0 = tk.Label(self.frameRight, text=' ')
        self.txt0.grid(column=0, row=5, sticky='W')

        self.txt4 = tk.Label(self.frameRight, text='Exibir ')
        self.txt4.grid(column=1, row=6, sticky='W')

        self.cb3 = tk.Checkbutton(self.frameRight, text='Número total de linhas', variable=self.cbVar3)
        self.cb3.grid(column=1, row=7, sticky='W')

        self.cb3 = tk.Checkbutton(self.frameRight, text='Total de registros de banco', variable=self.cbVar4)
        self.cb3.grid(column=1, row=8, sticky='W')

        self.cb3 = tk.Checkbutton(self.frameRight, text='Tamanho em bytes da tabela', variable=self.cbVar5)
        self.cb3.grid(column=1, row=9, sticky='W')

        self.cb3 = tk.Checkbutton(self.frameRight, text='Tamanho em bytes do banco', variable=self.cbVar6)
        self.cb3.grid(column=1, row=10, sticky='W')

        self.buttonGerar = tk.Button(self.frameRight, text="Gerar")
        self.buttonGerar.grid(column=3, row=6, sticky='E')

        self.buttonLimpar = tk.Button(self.frameRight, text="Limpar")
        self.buttonLimpar.grid(column=4, row=6, sticky='W')

        # Empacota os frames
        self.frameLeft.grid(column=0, row=0)
        self.frameRight.grid(column=1, row=0)
        
        # Inicia o mainloop
        tk.mainloop()

    # Função de callback para o okButton    
    def mostraEscolha(self):
        # cria uma mensagem
        self.message = 'Você selecionou:\n'
        # Verifica quais CheckButtons foram selecionados
        # e monta a mensagem 
        if self.cbVar1.get() == 1:
            self.message = self.message + '1\n'
        if self.cbVar2.get() == 1:
            self.message = self.message + '2\n'
        if self.cbVar3.get() == 1:
            self.message = self.message + '3\n'
        # Mostra a mensagem no messagebox
        messagebox.showinfo('Seleção', self.message)

def main():
   MyGUI()

main()