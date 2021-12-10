from sqlalchemy import MetaData
from mapeamento import *
from getTable import corrigeNome, getTable

def dbCount(session):
    tables = [Comercio, Usuario, Avaliacao, Localizacao, Transacao]
    total = int()

    for table in tables:
        total += session.query(table).count()
    
    return total

def tableCount(table, session):
    # Função para retornar o número total de registros em uma tabela
    return session.query(table).count()


def tableSize(dburi, table_name, flag):
    # Função para consultar o tamanho em bytes de uma tabela e/ou do banco todo

    m = MetaData(dburi)
    e = lambda x: m.bind.execute(x).first()[0] # Função anonima que executa a query
    m.reflect()
    q_pretty_size = "SELECT pg_size_pretty(pg_total_relation_size('%s'))"
    q_pretty_total = "SELECT pg_size_pretty(pg_database_size('yelp'))"

    # A função pretty retorna o tamanho como "human-readable"
    if flag == 1:
        return e(q_pretty_size % table_name) # Une a string ao table_name
    else:
        return e(q_pretty_total)

def bootloader_exibir(session, dburi, table_name, valores_exibir):
    info = {}

    table_name = corrigeNome(table_name)
    
    if valores_exibir[0]: info['tableCount'] = tableCount(getTable(table_name), session)
    else: info['tableCount'] = None

    if valores_exibir[1]: info['dbCount'] = dbCount(session)
    else: info['dbCount'] = None

    if valores_exibir[2]: info['tableSize'] = tableSize(dburi, table_name, 1)
    else: info['tableSize'] = None

    if valores_exibir[3]: info['dbSize'] = tableSize(dburi, table_name, 0)
    else: info['dbSize'] = None

    return info