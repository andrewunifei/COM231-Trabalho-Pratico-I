from mapeamento import *

def getTable(table_name):
    if table_name == "Comercio": return Comercio
    elif table_name == "Usuario": return Usuario
    elif table_name == "Avaliacao": return Avaliacao
    elif table_name == "Localizacao": return Localizacao
    else: return Transacao