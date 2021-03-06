import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ponte import ponte
from relatorio import Relatorio

class MyGUI:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title('Relatório Ad-Hoc')
        self.janela.geometry('1025x340')
    
        self.frameRight = tk.Frame(self.janela)
        self.frameLeft = tk.Frame(self.janela)
  
        self.cbVar1 = tk.IntVar()
        self.cbVar2 = tk.IntVar()
        self.cbVar3 = tk.IntVar()
        self.cbVar4 = tk.IntVar()
        self.cbVar5 = tk.IntVar()
        self.cbVar6 = tk.IntVar()
        self.box1 = tk.StringVar()
        self.box1.trace('w', self.update)
        self.box2 = tk.StringVar()
        
        # Ajusta os IntVar objetos para 0
        self.cbVar1.set(0)
        self.cbVar2.set(0)
        self.cbVar3.set(0)
        self.cbVar4.set(0)
        self.cbVar5.set(0)
        self.cbVar6.set(0)

        self.listaAtributos = []
        self.listaAtributos2 = []

        # FrameLeft
        self.txt01 = tk.Label(self.frameLeft, text='Selecione a tabela: ')
        self.txt01.grid(column=0, row=0)

        self.combobox1 = ttk.Combobox(self.frameLeft, textvariable=self.box1)
        self.combobox1.grid(column=0, row=1)
        self.combobox1['values'] = ['Avaliação', 'Comércio', 'Localização', 'Transação', 'Usuário']

        self.txt000 = tk.Label(self.frameLeft, text=' ')
        self.txt000.grid(column=0, row=2)

        self.listbox = tk.Listbox(self.frameLeft, width=25)
        self.listbox.grid(column=0, row=3)

        self.listbox2 = tk.Listbox(self.frameLeft, width=25)
        self.listbox2.grid(column=1, row=3)

        self.txt000 = tk.Label(self.frameLeft, text=' ')
        self.txt000.grid(column=0, row=4)

        self.buttonInserir = tk.Button(self.frameLeft, text="Selecionar")
        self.buttonInserir.grid(column=0, row=5)
        self.buttonInserir.bind("<Button>", self.insereAtributo)

        self.buttonTirar = tk.Button(self.frameLeft, text="Remover")
        self.buttonTirar.grid(column=1, row=5)
        self.buttonTirar.bind("<Button>", self.removeAtributo)

        # FrameRight
        self.txt1 = tk.Label(self.frameRight, text='Filtros')
        self.txt1.grid(column=1, row=0, sticky='W')

        self.cb1 = tk.Checkbutton(self.frameRight, text='Data de ', variable=self.cbVar1, command=self.handleCampoData)
        self.cb1.grid(column=1, row=1, sticky='W')

        self.inputData1 = tk.Entry(self.frameRight, width=15, state='disabled')
        self.inputData1.grid(column=2, row=1, sticky='W')

        self.txt2 = tk.Label(self.frameRight, text=' até ')
        self.txt2.grid(column=3, row=1, sticky='W')

        self.inputData2 = tk.Entry(self.frameRight, width=15, state='disabled')
        self.inputData2.grid(column=4, row=1, sticky='W')

        self.cb2 = tk.Checkbutton(self.frameRight, text='Limite de linhas ', variable=self.cbVar2, command=self.handleCampoLimite)
        self.cb2.grid(column=1, row=2, sticky='W')

        self.inputData3 = tk.Entry(self.frameRight, width=15, state='disabled')
        self.inputData3.grid(column=2, row=2, sticky='W')

        self.txt00 = tk.Label(self.frameRight, text=' ')
        self.txt00.grid(column=0, row=3, sticky='W')

        self.txt0 = tk.Label(self.frameRight, text=' ')
        self.txt0.grid(column=0, row=5, sticky='W')

        self.txt4 = tk.Label(self.frameRight, text='Exibir ')
        self.txt4.grid(column=1, row=6, sticky='W')

        self.cb3 = tk.Checkbutton(self.frameRight, text='Total de registro na tabela', variable=self.cbVar3)
        self.cb3.grid(column=1, row=7, sticky='W')

        self.cb3 = tk.Checkbutton(self.frameRight, text='Total de registros no banco', variable=self.cbVar4)
        self.cb3.grid(column=1, row=8, sticky='W')

        self.cb3 = tk.Checkbutton(self.frameRight, text='Tamanho em bytes da tabela', variable=self.cbVar5)
        self.cb3.grid(column=1, row=9, sticky='W')

        self.cb3 = tk.Checkbutton(self.frameRight, text='Tamanho em bytes do banco', variable=self.cbVar6)
        self.cb3.grid(column=1, row=10, sticky='W')

        self.txtUser = tk.Label(self.frameRight, text='Usuário do BD: ')
        self.txtUser.grid(column=3, row=6, sticky='W')
        self.inputUser = tk.Entry(self.frameRight, width=15)
        self.inputUser.grid(column=3, row=7, sticky='W')

        self.txtSenha = tk.Label(self.frameRight, text='Senha: ')
        self.txtSenha.grid(column=3, row=8, sticky='W')
        self.inputSenha = tk.Entry(self.frameRight, show= '*', width=15)
        self.inputSenha.grid(column=3, row=9, sticky='W')

        self.buttonGerar = tk.Button(self.frameRight, text="Gerar", command=self.Gerar)
        self.buttonGerar.grid(column=2, row=11, sticky='E')

        self.buttonLimpar = tk.Button(self.frameRight, text="Limpar", command=self.Limpar)
        self.buttonLimpar.grid(column=3, row=11, sticky='W')

        # Empacota os frames
        self.frameLeft.grid(column=0, row=0)
        self.frameRight.grid(column=1, row=0)
        
        # Inicia o mainloop
        tk.mainloop()

    def update(self, var, indx, mode):
        self.listbox.delete(0, tk.END)
        self.listbox2.delete(0, tk.END)
        tabelaSel = self.box1.get()
        if(tabelaSel == 'Avaliação'):
           self.listaAtributos = ['id_comercio', 'id_usuario', 'id', 'nota', 'texto', 'data', 'horario']
           self.cb1.config(state='normal')
           self.txt2.config(state='normal')
        else:
           self.cbVar1.set(0)
           self.inputData1.delete(0, tk.END)
           self.inputData2.delete(0, tk.END)
           self.cb1.config(state='disabled')
           self.txt2.config(state='disabled')
        if(tabelaSel == 'Comércio'):
           self.listaAtributos = ['id', 'nome', 'fechado', 'telefone', 'preco', 'pseudonimo', 'titulo_categoria', 'pseudonimo_categoria', 'quant_avaliacoes']
        elif(tabelaSel == 'Localização'):
           self.listaAtributos = ['id_comercio', 'id', 'cod_postal', 'pais', 'estado', 'cidade', 'logradouro']
        elif(tabelaSel == 'Transação'):
           self.listaAtributos = ['id_comercio', 'id', 'tipo']
        elif(tabelaSel == 'Usuário'):
           self.listaAtributos = ['id', 'nome']
        for titulo in self.listaAtributos:
           self.listbox.insert(tk.END, titulo)
    
    def handleCampoData(self):
        if self.cbVar1.get() == 0:
            self.inputData1.config(state='disabled')
            self.inputData2.config(state='disabled')
        else:
            self.inputData1.config(state='normal')
            self.inputData2.config(state='normal')

    def handleCampoLimite(self):
        if self.cbVar2.get() == 0:
            self.inputData3.delete(0, tk.END)
            self.inputData3.config(state='disabled')        
        else:
            self.inputData3.config(state='normal')

    def insereAtributo(self, event):
        atributoSel = self.listbox.get(tk.ACTIVE)
        self.listbox.delete(tk.ACTIVE)
        self.insereListBox2(atributoSel)

    def insereListBox2(self, atributo):
        self.listbox2.insert(tk.END, atributo)

    def removeAtributo(self, event):
        atributoSel = self.listbox2.get(tk.ACTIVE)
        self.listbox2.delete(tk.ACTIVE)
        self.insereListBox(atributoSel)

    def insereListBox(self, atributo):
        self.listbox.insert(tk.END, atributo)

    def Gerar(self):
        tabela = self.combobox1.get()
        user = self.inputUser.get()
        senha = self.inputSenha.get()
        if(tabela == '' or user == '' or senha == ''):
            if(tabela == ''):
                messagebox.showerror('ERRO!', 'Selecione uma tabela!')
            elif(user == ''):
                messagebox.showerror('ERRO!', 'Entre com o usuário do banco de dados!')
            elif(senha == ''):
                messagebox.showerror('ERRO!', 'Entre com a senha do banco de dados!')
        else:
            self.dicFiltro = {}
            self.listaExibir = []

            if(self.cbVar1.get() == 1):
                self.dicFiltro['data'] = [self.inputData1.get(), self.inputData2.get()]
            else:
                self.dicFiltro['data'] = [None, None]

            if(self.cbVar2.get() == 1):
                self.dicFiltro['limite'] = self.inputData3.get()
            else:
                self.dicFiltro['limite'] = None

            self.listaExibir.append(self.cbVar3.get())
            self.listaExibir.append(self.cbVar4.get())
            self.listaExibir.append(self.cbVar5.get())
            self.listaExibir.append(self.cbVar6.get())
            
            atributos = list(self.listbox2.get(0, tk.END))

            info_exibir, info_filtros = ponte(user, senha, tabela, self.listaExibir, self.dicFiltro)
            d = dict()
                
            for atributo in atributos:
                d[atributo] = []
                for registro in info_filtros:
                    d[atributo].append(getattr(registro, atributo))
            Relatorio(info_exibir, d, atributos)

    def Limpar(self):
        self.cbVar1.set(0)
        self.cbVar2.set(0)
        self.cbVar3.set(0)
        self.cbVar4.set(0)
        self.cbVar5.set(0)
        self.cbVar6.set(0)
        self.inputData1.delete(0, tk.END)
        self.inputData2.delete(0, tk.END)
        self.inputData3.delete(0, tk.END)
        self.inputUser.delete(0, tk.END)
        self.inputSenha.delete(0, tk.END)
        self.box1.set('')
        self.listbox.delete(0, tk.END)
        self.listbox2.delete(0, tk.END)
        self.inputData3.config(state='disabled') 
    
def main():
    MyGUI()

if __name__ == '__main__': main()