import tkinter as tk
from tkinter import ttk
from tkinter import Scrollbar
from tkinter.constants import CENTER, NO, RIGHT, BOTTOM, X, Y, LEFT

class Relatorio:
    def __init__(self, info_exibir, d, atributos):
        self.info_exibir = info_exibir
        self.d = d
        self.atributos = atributos

        root = tk.Tk()
        root.title('Relatório')
        root.geometry('1000x400')

        #BARRA DE ROLAGEM VERTICAL
        scrollbarY = Scrollbar(root)
        scrollbarY.pack(side = RIGHT, fill = Y)

        #BARRA DE ROLAGEM HORIZONTAL
        scrollbarX = Scrollbar(root, orient='horizontal')
        scrollbarX.pack(side = BOTTOM, fill = X)

        self.txt00 = tk.Label(root, text='')
        self.txt00.pack()
        #TEXTO SUPERIOR
        if(self.info_exibir['tableCount'] != None):
            self.txt01 = tk.Label(root, text='Total de registros na tabela: ' + str(self.info_exibir['tableCount']))
            self.txt01.pack()
        if(self.info_exibir['dbCount'] != None):
            self.txt02 = tk.Label(root, text='Total de registros no banco: ' + str(self.info_exibir['dbCount']))
            self.txt02.pack()
        if(self.info_exibir['tableSize'] != None):
            self.txt03 = tk.Label(root, text='Tamanho em bytes da tabela: ' + str(self.info_exibir['tableSize']))
            self.txt03.pack()
        if(self.info_exibir['dbSize'] != None):
            self.txt04 = tk.Label(root, text='Tamanho em bytes do banco: ' + str(self.info_exibir['dbSize']))
            self.txt04.pack()
        self.txt000 = tk.Label(root, text='')
        self.txt000.pack()

        #TABELA (DEFINIR yscrollcommand E xscrollcommand)
        tabela = ttk.Treeview(root, yscrollcommand = scrollbarY.set, xscrollcommand = scrollbarX.set)

        tabela['columns'] = [atributo for atributo in self.atributos]

        tabela.column("#0", width=0,  stretch=NO)
        for atributo in self.atributos:
            tabela.column(atributo,anchor=CENTER)
        
        tabela.heading("#0",text="",anchor=CENTER)
        for atributo in self.atributos:
            tabela.heading(atributo,text=atributo,anchor=CENTER)

        chaves = list(self.d.keys())
        registros = []
        id = 0

        for i in range(len(self.d[chaves[0]])):
            for chave in chaves:
                registros.append(self.d[chave][i])
            tabela.insert(parent='', index='end', iid=id, text='', values=registros)
            id += 1
            registros = []

        tabela.pack(fill=Y,expand=1)

        #CONFIGURAR BARRAS DE ROLAGEM NA TABELA
        scrollbarY.config(command = tabela.yview)
        scrollbarX.config(command = tabela.xview)

        tk.mainloop()