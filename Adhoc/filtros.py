from sqlalchemy import and_
from getTable import getTable

def consulta(session, nome_tabela, valores_filtros):
    tabela = getTable(nome_tabela)

    if valores_filtros['data'][0] != None:
        return session.query(tabela)\
            .filter(and_(tabela.data >= valores_filtros['data'][0], tabela.data < valores_filtros['data'][1])).all()

def bootloader_filtros(session, nome_tabela, valores_filtros):
    info = {}

    info['datas'] = consulta(session, nome_tabela, valores_filtros)

    return info