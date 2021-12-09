import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, Scrollbar, Listbox
from tkinter.constants import CENTER, NO, RIGHT, BOTTOM, X, Y, LEFT, BOTH, END

class Relatorio:
    def __init__(self, info_exibir, info_filtros):
        self.info_exibir = info_exibir
        self.info_filtros = info_filtros

        root = tk.Tk()
        root.title('Relatório')
        root.geometry('300x300')

        #BARRA DE ROLAGEM VERTICAL
        scrollbar = Scrollbar(root)
        scrollbar.pack(side = RIGHT, fill = Y)

        #BARRA DE ROLAGEM HORIZONTAL
        scrollbar2 = Scrollbar(root, orient='horizontal')
        scrollbar2.pack(side = BOTTOM, fill = X)

        #TEXTO SUPERIOR
        self.txt01 = tk.Label(root, text=self.info_exibir['tableCount'])
        self.txt01.pack()
        self.txt02 = tk.Label(root, text='Mussum Ipssum')
        self.txt02.pack()
        self.txt03 = tk.Label(root, text='Mussum Ipssum')
        self.txt03.pack()

        #TABELA (DEFINIR yscrollcommand E xscrollcommand)
        my_game = ttk.Treeview(root, yscrollcommand = scrollbar.set, xscrollcommand = scrollbar2.set)

        my_game['columns'] = ('player_id', 'player_name', 'player_Rank', 'player_states', 'player_city')

        my_game.column("#0", width=0,  stretch=NO)
        my_game.column("player_id",anchor=CENTER, width=80)
        my_game.column("player_name",anchor=CENTER,width=80)
        my_game.column("player_Rank",anchor=CENTER,width=80)
        my_game.column("player_states",anchor=CENTER,width=80)
        my_game.column("player_city",anchor=CENTER,width=80)

        my_game.heading("#0",text="",anchor=CENTER)
        my_game.heading("player_id",text="Id",anchor=CENTER)
        my_game.heading("player_name",text="Name",anchor=CENTER)
        my_game.heading("player_Rank",text="Rank",anchor=CENTER)
        my_game.heading("player_states",text="States",anchor=CENTER)
        my_game.heading("player_city",text="States",anchor=CENTER)

        my_game.insert(parent='',index='end',iid=0,text='TESTEEEE',
        values=('1','Ninja','101','Oklahoma', 'Moore'))
        my_game.insert(parent='',index='end',iid=1,text='',
        values=('2','Ranger','102','Wisconsin', 'Green Bay'))
        my_game.insert(parent='',index='end',iid=2,text='',
        values=('3','Deamon','103', 'California', 'Placentia'))
        my_game.insert(parent='',index='end',iid=3,text='',
        values=('4','Dragon','104','New York' , 'White Plains'))
        my_game.insert(parent='',index='end',iid=4,text='',
        values=('5','CrissCross','105','California', 'San Diego'))
        my_game.insert(parent='',index='end',iid=5,text='',
        values=('6','ZaqueriBlack','106','Wisconsin' , 'TONY'))
        my_game.insert(parent='',index='end',iid=6,text='',
        values=('6','ZaqueriBlack','106','Wisconsin' , 'TONY'))
        my_game.insert(parent='',index='end',iid=7,text='',
        values=('6','ZaqueriBlack','106','Wisconsin' , 'TONY'))
        my_game.insert(parent='',index='end',iid=8,text='',
        values=('6','ZaqueriBlack','106','Wisconsin' , 'TONY'))
        my_game.insert(parent='',index='end',iid=9,text='',
        values=('6','ZaqueriBlack','106','Wisconsin' , 'TONY'))
        my_game.insert(parent='',index='end',iid=10,text='',
        values=('6','ZaqueriBlack','106','Wisconsin' , 'TONY'))
        my_game.insert(parent='',index='end',iid=11,text='',
        values=('6','ZaqueriBlack','106','Wisconsin' , 'TONY'))
        my_game.insert(parent='',index='end',iid=12,text='',
        values=('6','ZaqueriBlack','106','Wisconsin' , 'TONY'))
        my_game.insert(parent='',index='end',iid=13,text='',
        values=('6','ZaqueriBlack','106','Wisconsin' , 'TONY'))
        my_game.insert(parent='',index='end',iid=14,text='',
        values=('6','ZaqueriBlack','106','Wisconsin' , 'TONY'))
        my_game.insert(parent='',index='end',iid=15,text='',
        values=('6','ZaqueriBlack','106','Wisconsin' , 'TONY'))
        my_game.insert(parent='',index='end',iid=16,text='',
        values=('6','ZaqueriBlack','106','Wisconsin' , 'TONY'))
        my_game.insert(parent='',index='end',iid=17,text='',
        values=('6','ZaqueriBlack','106','Wisconsin' , 'TONY'))
        my_game.insert(parent='',index='end',iid=18,text='',
        values=('6','ZaqueriBlack','106','Wisconsin' , 'TONY'))
        my_game.insert(parent='',index='end',iid=19,text='',
        values=('6','ZaqueriBlack','106','Wisconsin' , 'TONY'))
        my_game.insert(parent='',index='end',iid=20,text='',
        values=('6','ZaqueriBlack','106','Wisconsin' , 'TONY'))

        my_game.pack()

        #CONFIGURAR BARRAS DE ROLAGEM NA TABELA
        scrollbar.config( command = my_game.yview )
        scrollbar2.config( command = my_game.xview )

        tk.mainloop()


# def main():
#     Relatorio([], [])

# main()