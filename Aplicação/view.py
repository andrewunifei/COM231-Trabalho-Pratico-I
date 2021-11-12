from decimal import *
from datetime import datetime

class View():
    def imprimeStatus(self, status):
        if (status == 'sucesso'):
            print("Comando executado no banco de dados com sucesso")
        else:
            print(status)