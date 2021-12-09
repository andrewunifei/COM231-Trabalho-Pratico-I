from sqlalchemy import MetaData
from mapeamento import *
from getTable import getTable

def dbCount(session):
    tables = [Comercio, Usuario, Avaliacao, Localizacao, Transacao]
    total = int()

    for table in tables:
        total += session.query(table).count()
    
    return total

def tableCount(table, session):
    # Função para retornar o número total de registros em uma tabela
    return session.query(table).count()


def tableSize(dburi, table_name, wholedb):
    # Função para consultar o tamanho em bytes de uma tabela e/ou do banco todo

    t = dict()
    m = MetaData(dburi)
    e = lambda x: m.bind.execute(x).first()[0] # Função anonima que executa a query
    m.reflect()
    q_pretty_size = "SELECT pg_size_pretty(pg_total_relation_size('%s'))"
    q_pretty_total = "SELECT pg_size_pretty(pg_database_size('yelp'))"

    # A função pretty retorna o tamanho como "human-readable"
    t['size'] = e(q_pretty_size % table_name) # Une a string ao table_name

    if wholedb:
        t['total'] = e(q_pretty_total)
    else:
        t['total'] = None
    
    return t

def bootloader_exibir(session, dburi, table_name, valores_exibir):
    info = {}
    
    if valores_exibir[0]: info['tableCount'] = tableCount(getTable(table_name), session)
    else: info['tableCount'] = None

    if valores_exibir[1]: info['dbCount'] = dbCount(session)
    else: info['dbCount'] = None

    if valores_exibir[2]: info['tableSize'] = tableSize(dburi, table_name, valores_exibir[3])
    else: info['tableSize'] = None

    return info