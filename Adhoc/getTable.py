from mapeamento import *

def getTable(table_name):
    if table_name == "Comercio": return Comercio
    elif table_name == "Usuario": return Usuario
    elif table_name == "Avaliacao": return Avaliacao
    elif table_name == "Localizacao": return Localizacao
    else: return Transacao

def corrigeNome(table_name):
    if table_name == "Comércio": return "comercio"
    elif table_name == "Avaliação": return "avaliacao"
    elif table_name == "Localização": return "localizacao"
    elif table_name == "Usuário": return "usuario"
    else: return "transacao"
