import tkinter as tk
from tkinter import ttk
from tkinter import Scrollbar
from tkinter.constants import CENTER, NO, RIGHT, BOTTOM, X, Y

class Relatorio:
    def __init__(self, info_exibir, info_filtros):
        self.info_exibir = info_exibir
        self.info_filtros = info_filtros

        root = tk.Tk()
        root.title('Relatório')
        self.janela.geometry('1000x500')

        #BARRA DE ROLAGEM VERTICAL
        scrollbarY = Scrollbar(root)
        scrollbarY.pack(side = RIGHT, fill = Y)

        #BARRA DE ROLAGEM HORIZONTAL
        scrollbarX = Scrollbar(root, orient='horizontal')
        scrollbarX.pack(side = BOTTOM, fill = X)

        #TEXTO SUPERIOR
        if(self.info_exibir['tableCount'] != None):
            self.txt01 = tk.Label(root, text='Total de registro na tabela: ' + self.info_exibir['tableCount'])
            self.txt01.pack()
        if(self.info_exibir['dbCount'] != None):
            self.txt02 = tk.Label(root, text='Total de registros no banco: ' + self.info_exibir['dbCount'])
            self.txt02.pack()
        if(self.info_exibir['tableSize'] != None):
            self.txt03 = tk.Label(root, text='Tamanho em bytes da tabela: ' + self.info_exibir['tableSize'])
            self.txt03.pack()
        if(self.info_exibir['dbSize'] != None):
            self.txt04 = tk.Label(root, text='Tamanho em bytes do banco: ' + self.info_exibir['dbSize'])
            self.txt04.pack()

        #TABELA (DEFINIR yscrollcommand E xscrollcommand)
        tabela = ttk.Treeview(root, yscrollcommand = scrollbarY.set, xscrollcommand = scrollbarX.set)

        tabela['columns'] = ('player_id', 'player_name', 'player_Rank', 'player_states', 'player_city')

        tabela.column("#0", width=0,  stretch=NO)
        tabela.column("player_id",anchor=CENTER, width=80)
        tabela.column("player_name",anchor=CENTER,width=80)
        tabela.column("player_Rank",anchor=CENTER,width=80)
        tabela.column("player_states",anchor=CENTER,width=80)
        tabela.column("player_city",anchor=CENTER,width=80)

        tabela.heading("#0",text="",anchor=CENTER)
        tabela.heading("player_id",text="Id",anchor=CENTER)
        tabela.heading("player_name",text="Name",anchor=CENTER)
        tabela.heading("player_Rank",text="Rank",anchor=CENTER)
        tabela.heading("player_states",text="States",anchor=CENTER)
        tabela.heading("player_city",text="States",anchor=CENTER)

        tabela.insert(parent='',index='end',iid=0,text='',
        values=('1','Ninja','101','Oklahoma', 'Moore'))
        tabela.insert(parent='',index='end',iid=1,text='',
        values=('2','Ranger','102','Wisconsin', 'Green Bay'))
        tabela.insert(parent='',index='end',iid=2,text='',
        values=('3','Deamon','103', 'California', 'Placentia'))
        tabela.insert(parent='',index='end',iid=3,text='',
        values=('4','Dragon','104','New York' , 'White Plains'))
        tabela.insert(parent='',index='end',iid=4,text='',
        values=('5','CrissCross','105','California', 'San Diego'))
        tabela.insert(parent='',index='end',iid=5,text='',
        values=('6','ZaqueriBlack','106','Wisconsin' , 'TONY'))
        tabela.insert(parent='',index='end',iid=6,text='',
        values=('6','ZaqueriBlack','106','Wisconsin' , 'TONY'))
        tabela.insert(parent='',index='end',iid=7,text='',
        values=('6','ZaqueriBlack','106','Wisconsin' , 'TONY'))
        tabela.insert(parent='',index='end',iid=8,text='',
        values=('6','ZaqueriBlack','106','Wisconsin' , 'TONY'))
        tabela.insert(parent='',index='end',iid=9,text='',
        values=('6','ZaqueriBlack','106','Wisconsin' , 'TONY'))
        tabela.insert(parent='',index='end',iid=10,text='',
        values=('6','ZaqueriBlack','106','Wisconsin' , 'TONY'))
        tabela.insert(parent='',index='end',iid=11,text='',
        values=('6','ZaqueriBlack','106','Wisconsin' , 'TONY'))
        tabela.insert(parent='',index='end',iid=12,text='',
        values=('6','ZaqueriBlack','106','Wisconsin' , 'TONY'))
        tabela.insert(parent='',index='end',iid=13,text='',
        values=('6','ZaqueriBlack','106','Wisconsin' , 'TONY'))
        tabela.insert(parent='',index='end',iid=14,text='',
        values=('6','ZaqueriBlack','106','Wisconsin' , 'TONY'))
        tabela.insert(parent='',index='end',iid=15,text='',
        values=('6','ZaqueriBlack','106','Wisconsin' , 'TONY'))
        tabela.insert(parent='',index='end',iid=16,text='',
        values=('6','ZaqueriBlack','106','Wisconsin' , 'TONY'))
        tabela.insert(parent='',index='end',iid=17,text='',
        values=('6','ZaqueriBlack','106','Wisconsin' , 'TONY'))
        tabela.insert(parent='',index='end',iid=18,text='',
        values=('6','ZaqueriBlack','106','Wisconsin' , 'TONY'))
        tabela.insert(parent='',index='end',iid=19,text='',
        values=('6','ZaqueriBlack','106','Wisconsin' , 'TONY'))
        tabela.insert(parent='',index='end',iid=20,text='',
        values=('6','ZaqueriBlack','106','Wisconsin' , 'TONY'))

        tabela.pack()

        #CONFIGURAR BARRAS DE ROLAGEM NA TABELA
        scrollbarY.config(command = tabela.yview)
        scrollbarX.config(command = tabela.xview)

        tk.mainloop()